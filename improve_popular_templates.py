#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
인기 템플릿에 실제 동작하는 코드 추가
"""

import os
import json
from pathlib import Path

# 개선할 주요 템플릿들
templates_to_improve = {
    "001_web_nextjs": {
        "files": {
            "app/page.tsx": """export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <div className="z-10 max-w-5xl w-full items-center justify-between font-mono text-sm">
        <h1 className="text-4xl font-bold mb-4">
          Welcome to Next.js!
        </h1>
        <p className="text-xl mb-8">
          Get started by editing <code className="font-mono bg-gray-100 px-2 py-1 rounded">app/page.tsx</code>
        </p>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <a
            className="group rounded-lg border border-transparent px-5 py-4 transition-colors hover:border-gray-300 hover:bg-gray-100"
            href="https://nextjs.org/docs"
            target="_blank"
            rel="noopener noreferrer"
          >
            <h2 className="mb-3 text-2xl font-semibold">
              Docs{' '}
              <span className="inline-block transition-transform group-hover:translate-x-1 motion-reduce:transform-none">
                -&gt;
              </span>
            </h2>
            <p className="m-0 max-w-[30ch] text-sm opacity-50">
              Find in-depth information about Next.js features and API.
            </p>
          </a>

          <a
            className="group rounded-lg border border-transparent px-5 py-4 transition-colors hover:border-gray-300 hover:bg-gray-100"
            href="https://nextjs.org/learn"
            target="_blank"
            rel="noopener noreferrer"
          >
            <h2 className="mb-3 text-2xl font-semibold">
              Learn{' '}
              <span className="inline-block transition-transform group-hover:translate-x-1 motion-reduce:transform-none">
                -&gt;
              </span>
            </h2>
            <p className="m-0 max-w-[30ch] text-sm opacity-50">
              Learn about Next.js in an interactive course with quizzes!
            </p>
          </a>
        </div>
      </div>
    </main>
  );
}
""",
            "app/layout.tsx": """import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import './globals.css';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: 'Next.js App',
  description: 'Created with Next.js',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="ko">
      <body className={inter.className}>{children}</body>
    </html>
  );
}
""",
            "app/globals.css": """@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  --foreground-rgb: 0, 0, 0;
  --background-start-rgb: 214, 219, 220;
  --background-end-rgb: 255, 255, 255;
}

@media (prefers-color-scheme: dark) {
  :root {
    --foreground-rgb: 255, 255, 255;
    --background-start-rgb: 0, 0, 0;
    --background-end-rgb: 0, 0, 0;
  }
}

body {
  color: rgb(var(--foreground-rgb));
  background: linear-gradient(
      to bottom,
      transparent,
      rgb(var(--background-end-rgb))
    )
    rgb(var(--background-start-rgb));
}
"""
        },
        "package_updates": {
            "dependencies": {
                "next": "14.0.4",
                "react": "^18.2.0",
                "react-dom": "^18.2.0"
            },
            "devDependencies": {
                "@types/node": "^20",
                "@types/react": "^18",
                "@types/react-dom": "^18",
                "autoprefixer": "^10.0.1",
                "postcss": "^8",
                "tailwindcss": "^3.3.0",
                "typescript": "^5"
            },
            "scripts": {
                "dev": "next dev",
                "build": "next build",
                "start": "next start",
                "lint": "next lint"
            }
        }
    },
    "1551_testing_jest": {
        "files": {
            "src/sum.js": """function sum(a, b) {
  return a + b;
}

module.exports = sum;
""",
            "src/sum.test.js": """const sum = require('./sum');

test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3);
});

test('adds -1 + 1 to equal 0', () => {
  expect(sum(-1, 1)).toBe(0);
});
""",
            "jest.config.js": """module.exports = {
  testEnvironment: 'node',
  coveragePathIgnorePatterns: ['/node_modules/'],
  testMatch: ['**/__tests__/**/*.js', '**/?(*.)+(spec|test).js'],
};
"""
        },
        "package_updates": {
            "dependencies": {},
            "devDependencies": {
                "jest": "^29.7.0"
            },
            "scripts": {
                "test": "jest",
                "test:watch": "jest --watch",
                "test:coverage": "jest --coverage"
            }
        }
    },
    "1553_testing_cypress": {
        "files": {
            "cypress/e2e/spec.cy.js": """describe('My First Test', () => {
  it('Visits the app', () => {
    cy.visit('http://localhost:3000');
    cy.contains('Welcome');
  });

  it('Clicks a button', () => {
    cy.visit('http://localhost:3000');
    cy.get('button').first().click();
  });
});
""",
            "cypress.config.js": """const { defineConfig } = require('cypress');

module.exports = defineConfig({
  e2e: {
    baseUrl: 'http://localhost:3000',
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
});
"""
        },
        "package_updates": {
            "devDependencies": {
                "cypress": "^13.6.0"
            },
            "scripts": {
                "cypress:open": "cypress open",
                "cypress:run": "cypress run"
            }
        }
    },
    "1793_state_redux": {
        "files": {
            "src/store.js": """import { configureStore } from '@reduxjs/toolkit';
import counterReducer from './features/counter/counterSlice';

export const store = configureStore({
  reducer: {
    counter: counterReducer,
  },
});
""",
            "src/features/counter/counterSlice.js": """import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  value: 0,
};

export const counterSlice = createSlice({
  name: 'counter',
  initialState,
  reducers: {
    increment: (state) => {
      state.value += 1;
    },
    decrement: (state) => {
      state.value -= 1;
    },
    incrementByAmount: (state, action) => {
      state.value += action.payload;
    },
  },
});

export const { increment, decrement, incrementByAmount } = counterSlice.actions;

export default counterSlice.reducer;
""",
            "src/App.js": """import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { increment, decrement, incrementByAmount } from './features/counter/counterSlice';

function App() {
  const count = useSelector((state) => state.counter.value);
  const dispatch = useDispatch();

  return (
    <div className="App">
      <h1>Redux Counter: {count}</h1>
      <button onClick={() => dispatch(increment())}>+</button>
      <button onClick={() => dispatch(decrement())}>-</button>
      <button onClick={() => dispatch(incrementByAmount(5))}>+5</button>
    </div>
  );
}

export default App;
"""
        },
        "package_updates": {
            "dependencies": {
                "@reduxjs/toolkit": "^2.0.1",
                "react": "^18.2.0",
                "react-dom": "^18.2.0",
                "react-redux": "^9.0.4"
            },
            "scripts": {
                "dev": "vite",
                "build": "vite build",
                "preview": "vite preview"
            }
        }
    },
    "1924_email_nodemailer": {
        "files": {
            "src/sendEmail.js": """const nodemailer = require('nodemailer');
require('dotenv').config();

// Create reusable transporter
const transporter = nodemailer.createTransporter({
  host: process.env.SMTP_HOST || 'smtp.gmail.com',
  port: process.env.SMTP_PORT || 587,
  secure: false, // true for 465, false for other ports
  auth: {
    user: process.env.SMTP_USER,
    pass: process.env.SMTP_PASS,
  },
});

async function sendEmail(to, subject, text, html) {
  try {
    const info = await transporter.sendMail({
      from: process.env.SMTP_FROM || '"App Name" <noreply@example.com>',
      to,
      subject,
      text,
      html,
    });

    console.log('Message sent: %s', info.messageId);
    return info;
  } catch (error) {
    console.error('Error sending email:', error);
    throw error;
  }
}

// Example usage
if (require.main === module) {
  sendEmail(
    'test@example.com',
    'Test Email',
    'This is a test email',
    '<b>This is a test email</b>'
  );
}

module.exports = { sendEmail, transporter };
""",
            ".env.example": """# Nodemailer Configuration
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASS=your-app-password
SMTP_FROM="Your Name" <your-email@gmail.com>
"""
        },
        "package_updates": {
            "dependencies": {
                "nodemailer": "^6.9.7",
                "dotenv": "^16.3.1"
            },
            "scripts": {
                "start": "node src/sendEmail.js",
                "test": "echo 'Run email test'"
            }
        }
    },
    "1934_payment_stripe": {
        "files": {
            "src/server.js": """const express = require('express');
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());
app.use(express.static('public'));

// Create payment intent
app.post('/create-payment-intent', async (req, res) => {
  try {
    const { amount, currency = 'usd' } = req.body;

    const paymentIntent = await stripe.paymentIntents.create({
      amount,
      currency,
      automatic_payment_methods: {
        enabled: true,
      },
    });

    res.json({
      clientSecret: paymentIntent.client_secret,
    });
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

// Webhook handler
app.post('/webhook', express.raw({ type: 'application/json' }), async (req, res) => {
  const sig = req.headers['stripe-signature'];
  let event;

  try {
    event = stripe.webhooks.constructEvent(req.body, sig, process.env.STRIPE_WEBHOOK_SECRET);
  } catch (err) {
    res.status(400).send(`Webhook Error: ${err.message}`);
    return;
  }

  switch (event.type) {
    case 'payment_intent.succeeded':
      console.log('Payment succeeded!', event.data.object);
      break;
    case 'payment_intent.payment_failed':
      console.log('Payment failed!', event.data.object);
      break;
    default:
      console.log(`Unhandled event type ${event.type}`);
  }

  res.json({ received: true });
});

app.listen(PORT, () => {
  console.log(`🚀 Server running on http://localhost:${PORT}`);
});
""",
            ".env.example": """# Stripe Keys
STRIPE_SECRET_KEY=sk_test_...
STRIPE_PUBLISHABLE_KEY=pk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...

# Server
PORT=3000
"""
        },
        "package_updates": {
            "dependencies": {
                "stripe": "^14.7.0",
                "express": "^4.18.2",
                "dotenv": "^16.3.1"
            },
            "scripts": {
                "start": "node src/server.js",
                "dev": "nodemon src/server.js"
            }
        }
    }
}

def improve_template(template_name, config):
    """템플릿 개선"""
    template_path = Path(template_name)

    if not template_path.exists():
        print(f"  ⚠️  {template_name} not found, skipping...")
        return False

    # 파일 생성
    if "files" in config:
        for file_path, content in config["files"].items():
            full_path = template_path / file_path
            full_path.parent.mkdir(parents=True, exist_ok=True)

            with open(full_path, "w", encoding="utf-8") as f:
                f.write(content)

    # package.json 업데이트
    if "package_updates" in config:
        package_json_path = template_path / "package.json"

        if package_json_path.exists():
            with open(package_json_path, "r", encoding="utf-8") as f:
                package_data = json.load(f)

            # 업데이트
            if "dependencies" in config["package_updates"]:
                package_data["dependencies"] = config["package_updates"]["dependencies"]

            if "devDependencies" in config["package_updates"]:
                package_data["devDependencies"] = config["package_updates"]["devDependencies"]

            if "scripts" in config["package_updates"]:
                package_data["scripts"] = config["package_updates"]["scripts"]

            with open(package_json_path, "w", encoding="utf-8") as f:
                json.dump(package_data, f, indent=2, ensure_ascii=False)

    return True

def main():
    """메인 함수"""
    print("🔧 주요 템플릿 개선 시작...\n")

    improved = 0
    failed = 0

    for template_name, config in templates_to_improve.items():
        print(f"📝 {template_name} 개선 중...")
        if improve_template(template_name, config):
            improved += 1
            print(f"  ✅ 완료")
        else:
            failed += 1

    print(f"\n✅ 개선 완료!")
    print(f"  - 성공: {improved}개")
    print(f"  - 실패: {failed}개")

if __name__ == "__main__":
    main()
