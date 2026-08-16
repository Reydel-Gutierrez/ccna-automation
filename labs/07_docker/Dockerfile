# Exam 4.6 — Interpret this Dockerfile.
# Each instruction creates a layer. Order matters for cache efficiency.

FROM python:3.12-slim

# Metadata is not required on the exam, but documents image intent.
LABEL exam.objective="4.6 Interpret contents of a Dockerfile"

WORKDIR /app

# Copy only what the app needs, then install nothing extra.
COPY app.py .

# Environment variables inside the container.
ENV PORT=8080
ENV APP_ENV=lab

EXPOSE 8080

# Default process. JSON-exec form is preferred (no shell).
CMD ["python", "app.py"]
