from pydantic import BaseModel


class JobSchema(BaseModel):
    role: str
    required_skills: list[str]
    preferred_skills: list[str]
    minimum_experience: float | None


job = JobSchema(
    role="SDE",
    required_skills=["Python", "Django", "Flask"],
    preferred_skills=["AWS", "Docker", "Kubernetes"],
    minimum_experience=2.0
)


print(job)

print(job.role)

print(job.required_skills)