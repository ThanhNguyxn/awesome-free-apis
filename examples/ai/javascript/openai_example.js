/**
 * OpenAI API Example - Text Generation with GPT
 * Documentation: https://platform.openai.com/docs/api-reference
 * Note: Requires API key (sign up for free trial credits)
 * Works in both Node.js and Browser
 */

// ⚠️ IMPORTANT: Set your API key as environment variable
// For Node.js: export OPENAI_API_KEY='your-api-key-here'
// For Browser: Replace process.env.OPENAI_API_KEY with your key (not recommended for production!)
const API_KEY = typeof process !== 'undefined' ? process.env.OPENAI_API_KEY : 'YOUR_KEY_HERE';

/**
 * Generate text completion using OpenAI's chat models
 * @param {string} prompt - Your question or instruction
 * @param {string} model - Model to use ('gpt-3.5-turbo' or 'gpt-4')
 * @param {number} maxTokens - Maximum length of response
 * @returns {Promise<object>} Generated response with token usage
 */
async function chatCompletion(prompt, model = 'gpt-3.5-turbo', maxTokens = 150) {
    if (!API_KEY || API_KEY === 'YOUR_KEY_HERE') {
        console.error("❌ Error: OPENAI_API_KEY not set!");
        console.error("Set it with: export OPENAI_API_KEY='your-key'");
        return null;
    }

    try {
        const url = 'https://api.openai.com/v1/chat/completions';

        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${API_KEY}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                model: model,
                messages: [
                    { role: 'user', content: prompt }
                ],
                max_tokens: maxTokens,
                temperature: 0.7  // Creativity level (0-2)
            })
        });

        if (!response.ok) {
            if (response.status === 401) {
                console.error("❌ Authentication failed! Check your API key.");
            } else if (response.status === 429) {
                console.error("❌ Rate limit exceeded or quota exhausted!");
            } else {
                console.error(`❌ HTTP error! status: ${response.status}`);
            }
            return null;
        }

        const result = await response.json();

        // Extract the generated text
        return {
            response: result.choices[0].message.content,
            tokensUsed: result.usage.total_tokens,
            model: result.model
        };

    } catch (error) {
        console.error('❌ Request failed:', error.message);
        return null;
    }
}

// Example usage
(async () => {
    console.log("🤖 OpenAI GPT Chat Example");
    console.log("=".repeat(50));

    // Example 1: Simple question
    const prompt1 = "Explain what an API is in one sentence.";
    console.log(`\n💬 Prompt: ${prompt1}`);

    const result = await chatCompletion(prompt1);
    if (result) {
        console.log(`\n🤖 Response: ${result.response}`);
        console.log(`📊 Tokens used: ${result.tokensUsed}`);
        console.log(`🏷️  Model: ${result.model}`);
    }

    // Example 2: Code generation
    console.log("\n" + "=".repeat(50));
    const prompt2 = "Write a JavaScript function to reverse a string.";
    console.log(`\n💬 Prompt: ${prompt2}`);

    const result2 = await chatCompletion(prompt2, 'gpt-3.5-turbo', 200);
    if (result2) {
        console.log(`\n🤖 Response:\n${result2.response}`);
    }

    // Example 3: Creative writing
    console.log("\n" + "=".repeat(50));
    const prompt3 = "Write a haiku about programming.";
    console.log(`\n💬 Prompt: ${prompt3}`);

    const result3 = await chatCompletion(prompt3, 'gpt-3.5-turbo', 50);
    if (result3) {
        console.log(`\n🤖 Response:\n${result3.response}`);
    }
})();

/**
 * 💡 Tips:
 * - Get free trial credits at: https://platform.openai.com/signup
 * - Keep your API key secret! Never commit it to GitHub
 * - Monitor usage at: https://platform.openai.com/usage
 * - gpt-3.5-turbo is cheaper and faster than gpt-4
 */

// For Node.js, export function
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { chatCompletion };
}
