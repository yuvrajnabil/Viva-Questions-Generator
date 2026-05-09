import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("API_KEY")
if not api_key:
    raise ValueError("Missing API key")

client = genai.Client(api_key=api_key)

# note Generator
def note_generator(images):

    prompt= """Use this prompt with any AI model. Upload the semester final question images together with this prompt.

```text
You are an expert academic interviewer, curriculum analyst, and exam pattern extractor.

Your task is to analyze the uploaded semester final exam question images and generate a COMPLETE interview preparation package from them.

IMPORTANT INSTRUCTIONS:

1. FIRST PHASE — DEEP EXAM ANALYSIS
- Carefully read EVERY uploaded question image.
- Extract ALL topics, subtopics, concepts, formulas, definitions, algorithms, proofs, derivations, coding problems, theoretical discussions, applications, and case studies.
- Do NOT skip any question, even small sub-questions or MCQ concepts.
- Identify repeated concepts and high-frequency topics.
- Detect the subject/domain automatically.
- Reconstruct unclear or partially visible text intelligently using context.
- Group related concepts into categorized topic sections.
- Build a hidden syllabus map internally before generating questions.

2. SECOND PHASE — INTERVIEW QUESTION GENERATION
Generate interview questions that comprehensively cover ALL extracted topics from the semester finals.

The interview questions must include:
- Fundamental conceptual questions
- Beginner-level interview questions
- Intermediate technical questions
- Advanced interview questions
- Problem-solving questions
- Scenario-based questions
- Viva-style oral questions
- Practical/application-based questions
- Definition-based questions
- Comparison questions
- “Why/how” reasoning questions
- Mathematical derivation/proof questions (if applicable)
- Coding/programming questions (if applicable)
- System design/architecture questions (if applicable)

3. ANSWER REQUIREMENTS
For EVERY interview question:
- Provide a clear and accurate answer.
- Give interview-style explanations.
- Include step-by-step reasoning where needed.
- Include formulas and derivations in proper LaTeX format.
- Include examples where useful.
- Mention common mistakes or traps interviewers may ask.
- Keep answers concise but technically strong.
- For programming questions:
  - provide optimized solutions,
  - explain time complexity,
  - explain space complexity,
  - include dry runs when necessary.

4. COVERAGE RULES (VERY IMPORTANT)
- DO NOT miss ANY topic from the semester final questions.
- Ensure 100% topic coverage.
- If a topic appears only once in the exam, still generate interview questions from it.
- Generate multiple interview questions for important/high-weight topics.
- Cover both theoretical and practical aspects.
- Cover hidden prerequisite concepts implied by the questions.

5. OUTPUT FORMAT

Generate output in the following structure:

# Subject Overview
- Detected subject/domain
- Main syllabus areas
- Important recurring themes

# Topic-wise Interview Questions

## Topic 1: [Topic Name]

### Basic Questions
Q1.
Answer:

Q2.
Answer:

### Intermediate Questions
Q1.
Answer:

### Advanced Questions
Q1.
Answer:

### Viva Questions
Q1.
Answer:

### Practical/Application Questions
Q1.
Answer:

(repeat for ALL topics)

# Most Important Interview Questions
- List the highest-priority questions likely to be asked in interviews.

# Rapid Revision Section
- Key formulas
- Key definitions
- Important theorems
- Common interview traps
- Frequently confused concepts

# Mock Interview Round
Generate:
- 20 rapid-fire viva questions
- 10 deep technical questions
- 5 scenario-based questions

6. QUALITY REQUIREMENTS
- Make the interview questions industry-level and academic-level.
- Make explanations technically accurate.
- Use professional interview language.
- Ensure no duplicated questions.
- Maintain logical ordering from easy → advanced.
- If the subject is mathematical or technical, use proper notation and LaTeX formatting.
- If images are blurry, infer intelligently instead of skipping content.
- Prioritize completeness and depth over brevity.

FINAL IMPORTANT RULE:
Your highest priority is COMPLETE TOPIC COVERAGE from the uploaded semester final questions. No concept from the exam should remain uncovered in the generated interview preparation material.
```
"""
    
    
    response=client.models.generate_content(
              model = "gemini-3-flash-preview",
              contents= [images, prompt]
             )

    return response.text
