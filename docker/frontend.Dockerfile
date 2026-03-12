FROM node:20

WORKDIR /app

# Copy frontend files
COPY frontend /app/frontend

WORKDIR /app/frontend

# Install dependencies
RUN npm install

# Build project
RUN npm run build

EXPOSE 5173

CMD ["npm", "run", "dev"]