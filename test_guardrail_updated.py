# -*- coding: utf-8 -*-
from deepeval import assert_test
from deepeval.models import GeminiModel
from deepeval.test_case import LLMTestCase
from deepeval.guardrails import (
    BaseGuard,
    Guardrails,
    PrivacyGuard,
    PromptInjectionGuard,
    JailbreakingGuard,
    ToxicityGuard,
    GraphicContentGuard,
    HallucinationGuard,
    IllegalGuard
)

def main():
    # Initialize the Gemini model
    eval_model = GeminiModel(
        model="gemini-pro",
        api_key=""
    )

    # Create test case
    test_case = LLMTestCase(
        input="How many articles are there in the Selenium webdriver python course?",
        actual_output="there are 23 articles in the course",
        context=[
            "Complete Understanding on Selenium Python API Methods with real time Scenarios on LIVE Websites\n"
            "\"Last but not least\" you can clear any Interview and can Lead Entire Selenium Python Projects from "
            "Design Stage\nThis course includes:\n17.5 hours on-demand video\nAssignments\n23 articles\n9 "
            "downloadable resources\nAccess on mobile and TV\nCertificate of completion\nRequirements",
            "What you'll learn\n*****By the end of this course,You will be Mastered on Selenium Webdriver with "
            "strong Core JAVA basics\n****You will gain the ability to design PAGEOBJECT, DATADRIVEN&HYBRID "
            "Automation FRAMEWORKS from scratch\n*** InDepth understanding of real time Selenium CHALLENGES with "
            "100 + examples\n*Complete knowledge on TestNG, MAVEN,ANT, JENKINS,LOG4J, CUCUMBER, HTML REPORTS,EXCEL "
            "API, GRID PARALLEL TESTING"
        ]
    )

    # Create guards
    guards = [
        PrivacyGuard(),
        PromptInjectionGuard(),
        JailbreakingGuard(),
        ToxicityGuard(),
        GraphicContentGuard(),
        HallucinationGuard(),
        IllegalGuard()
    ]

    # Create guardrails
    guardrails = Guardrails(guards=guards)

    # Run guardrails evaluation
    print("\n=== Running Guardrails Evaluation ===")
    
    for guard in guards:
        print(f"\nChecking {guard.__class__.__name__}...")
        
        # Try different methods that might exist
        methods = ['evaluate', 'run', 'check', 'verify', 'validate', 'measure']
        success = False
        
        for method_name in methods:
            if hasattr(guard, method_name):
                try:
                    method = getattr(guard, method_name)
                    if method_name == 'measure':
                        result = method(test_case)
                    else:
                        result = method(test_case.input, test_case.actual_output)
                    print(f"Method '{method_name}' succeeded")
                    print(f"Result: {result}")
                    success = True
                    break
                except Exception as e:
                    print(f"Method '{method_name}' failed: {str(e)}")
        
        if not success:
            print("No working evaluation method found")

if __name__ == "__main__":
    main()
