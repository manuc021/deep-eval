# -*- coding: utf-8 -*-
import os
from deepeval.models import GeminiModel
from deepeval.test_case import LLMTestCase
from deepeval import assert_test

# ===== Guardrails imports =====
from deepeval.guardrails.cybersecurity_guard import CyberattackCategory
from deepeval.guardrails import (
    PrivacyGuard,
    PromptInjectionGuard,
    JailbreakingGuard,
    GraphicContentGuard,
    HallucinationGuard,
    IllegalGuard,
    ModernizationGuard,
    SyntaxGuard,
    TopicalGuard,
    ToxicityGuard,
    CybersecurityGuard,
    GuardType,
    Guardrails
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

    # Setup guardrails
    privacy_guard = PrivacyGuard()
    prompt_injection_guard = PromptInjectionGuard()
    jailbreaking_guard = JailbreakingGuard()
    graphic_content_guard = GraphicContentGuard()
    hallucination_guard = HallucinationGuard()
    illegal_guard = IllegalGuard()
    modernization_guard = ModernizationGuard()
    syntax_guard = SyntaxGuard()
    toxicity_guard = ToxicityGuard()
    cyber_security_guard = CybersecurityGuard(
        purpose="Ensure input and output are free from security vulnerabilities",
        categories=[category for category in CyberattackCategory]
    )

    guardrails = Guardrails(
        guards=[
            privacy_guard,
            prompt_injection_guard,
            jailbreaking_guard,
            graphic_content_guard,
            hallucination_guard,
            illegal_guard,
            modernization_guard,
            syntax_guard,
            toxicity_guard,
            cyber_security_guard,
        ]
    )

    # Run guardrails
    print("\n=== Running Guardrails ===")
    for guard in guardrails.guards:
        result = guard.run(test_case.input, test_case.actual_output)
        print(f"\nGuard: {guard.__class__.__name__}")
        print(f"Passed: {result.passed}")
        if not result.passed:
            print(f"Reason: {result.reason}")

if __name__ == "__main__":
    main()
