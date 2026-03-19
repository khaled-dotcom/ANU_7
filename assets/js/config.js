/**
 * Public chatbot config
 *
 * This file is loaded by index.html and read by app.js via the global CONFIG object.
 * Keep real secrets on a backend service in production.
 */
const CONFIG = {
  // Production: API key is handled securely via backend proxy.
  GROQ_API_KEY: '',
  GROQ_API_URL: 'https://api.groq.com/openai/v1/chat/completions',
  GROQ_MODEL: 'llama3-8b-8192'
};


