FROM node:18-alpine as frontend-build

WORKDIR /app
COPY ./frontend/package.json ./frontend/package-lock.json ./
RUN npm ci
COPY ./frontend ./
RUN npm run build

FROM python:3.11-slim as backend

WORKDIR /app

# Copy FastAPI backend files
COPY ./backend ./backend
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements.txt

# Copy frontend build artifact to backend static directory
COPY --from=frontend-build /app/dist /app/backend/app/static

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
