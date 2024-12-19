'use client';
import Head from 'next/head';
import Image from 'next/image';
import { useState } from 'react';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000';

interface LearningContent {
  explanation: string;
  image_path: string;
}

export default function Home() {
  const [topic, setTopic] = useState('');
  const [learningStyle, setLearningStyle] = useState('standard');
  const [content, setContent] = useState<LearningContent | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const learningStyles = [
    'standard', 
    'visual', 
    'auditory', 
    'kinesthetic'
  ];

  const generateContent = async () => {
    if (!topic) {
      setError('Please enter a topic');
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const response = await fetch(`${API_BASE_URL}/generate-content`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          topic,
          learning_style: learningStyle
        })
      });

      if (!response.ok) {
        throw new Error('Failed to generate content');
      }

      const data = await response.json();
      setContent(data);
    } catch (err) {
      setError('Failed to generate content. Please try again.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <Head>
        <title>Educational Content Generator</title>
        <meta name="description" content="Generate personalized learning content" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className="max-w-2xl mx-auto bg-white shadow-md rounded-lg p-6">
        <h1 className="text-3xl font-bold mb-6 text-center">
          Educational Assistant
        </h1>

        <div className="mb-4">
          <label className="block text-gray-700 font-bold mb-2">
            Learning Topic
          </label>
          <input 
            type="text"
            value={topic}
            onChange={(e) => setTopic(e.target.value)}
            placeholder="Enter a topic to learn about"
            className="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-gray-700"
          />
        </div>

        <div className="mb-4">
          <label className="block text-gray-700 font-bold mb-2">
            Learning Style
          </label>
          <select
            value={learningStyle}
            onChange={(e) => setLearningStyle(e.target.value)}
            className="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-gray-700"
          >
            {learningStyles.map(style => (
              <option key={style} value={style}>
                {style.charAt(0).toUpperCase() + style.slice(1)} Learner
              </option>
            ))}
          </select>
        </div>

        <button 
          onClick={generateContent}
          disabled={loading}
          className="w-full bg-blue-500 text-white py-2 rounded-lg hover:bg-blue-600 transition duration-300 disabled:opacity-50"
        >
          {loading ? 'Generating...' : 'Generate Content'}
        </button>

        {error && (
          <div className="mt-4 text-red-500 text-center">
            {error}
          </div>
        )}

        {content && (
          <div className="mt-6">
            <h2 className="text-2xl font-bold mb-4 colour:blue">Learning Content</h2>
            
            <div className="bg-gray-50 p-4 rounded-lg mb-4">
              <h3 className="font-bold mb-2 colour:blue">Explanation:</h3>
              <p className="text-gray-700">{content.explanation}</p>
            </div>

            <div className="text-center">
              <h3 className="font-bold mb-2">Educational Image:</h3>
              <img 
                src={`${API_BASE_URL}${content.image_path}`} 
                alt="Educational Content"
                className="mx-auto max-w-full h-auto rounded-lg shadow-md"
              />
            </div>
          </div>
        )}
      </main>
    </div>
  );
}