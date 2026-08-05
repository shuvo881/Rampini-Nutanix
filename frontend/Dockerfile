ARG BACKEND_URL=http://backend:8000

# ---------- Dependencies ----------
FROM node:20-alpine AS deps

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm ci

# ---------- Builder ----------
FROM node:20-alpine AS builder

ARG BACKEND_URL=http://backend-service:8000
ENV BACKEND_URL=${BACKEND_URL}
WORKDIR /app

COPY --from=deps /app/node_modules ./node_modules
COPY . .

RUN npm run build

# ---------- Runtime ----------
FROM node:20-alpine AS runner

ARG BACKEND_URL=http://backend:8000
ENV NODE_ENV=production
ENV BACKEND_URL=${BACKEND_URL}
WORKDIR /app

COPY --from=builder /app/package.json ./
COPY --from=builder /app/package-lock.json ./
COPY --from=builder /app/next.config.ts ./
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/node_modules ./node_modules

EXPOSE 3000

CMD ["npm", "run", "start"]