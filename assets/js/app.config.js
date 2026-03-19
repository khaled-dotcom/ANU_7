/**
 * Chatbot configuration (client-side)
 *
 * IMPORTANT:
 * - Do NOT put a real API key in client-side code for production.
 * - For a real deployment, you should call your own backend, which then calls Groq securely.
 * - This file is only for local demos or development.
 */
const CONFIG = {
  // Production: API key is handled securely via backend proxy.
  GROQ_API_KEY: '',
  GROQ_API_URL: 'https://api.groq.com/openai/v1/chat/completions',
  GROQ_MODEL: 'openai/gpt-oss-120b'
};

