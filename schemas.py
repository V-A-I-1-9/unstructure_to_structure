"""
This file defines the expected output schemas
for each transformation.

These schemas act as contracts between the LLM
and the application.
"""


ACTION_PLAN_SCHEMA = {
    "goal": "string",
    "steps": ["string"],
    "deliverables": ["string"],
    "estimated_time": "string"
}


PROJECT_BLUEPRINT_SCHEMA = {
    "problem_summary": "string",
    "target_users": ["string"],
    "proposed_solution": "string",
    "core_features": ["string"],
    "tech_stack": ["string"],
    "mvp_scope": "string"
}


CHECKLIST_SCHEMA = {
    "task_category": "string",
    "checklist": [
        {
            "item": "string",
            "status": "string"
        }
    ]
}
