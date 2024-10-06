# GLOBE Environmental Awareness Game

Welcome to the **GLOBE Environmental Awareness Game**! This Telegram-based text adventure game is designed to educate players about environmental science and issues through interactive storytelling and decision-making. Players will navigate various scenarios related to global and local environmental challenges while utilizing data from the Global Learning and Observations to Benefit the Environment (GLOBE) program.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)

## Project Overview

This project aims to create an engaging and educational platform for users to explore environmental topics through a text-based game format. Players make choices that affect the outcome of the game, all while learning about critical environmental issues such as urbanization, water pollution, droughts, heatwaves, and floods.

## Features

- Interactive storytelling with decision-making
- Integration with GLOBE protocols for real-world data
- AI-generated images to enhance the gaming experience
- Educational content about environmental issues
- User-friendly interface via Telegram bot

### Key Components

- **API Routes**: Handles incoming requests and connects to the relevant services.
- **Models**: Defines the data structure used in the game and the interaction with GLOBE protocols.
- **Services**: Contains business logic for accessing GLOBE data and game mechanics.
- **Utils**: Helper functions for data processing and utility functions.

## Setup Instructions

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yuriimartyniuk/NasaSpageAppChallenge2024.git
   cd NasaSpageAppChallenge2024

   python main.py
## DONT FORGET USE YOUR OWN TOKENS IN ENV FILE
Example:

```bash
BOT_TOKEN=your_telegram_bot_token
OPENAI_API_KEY=your_openai_api_key
MONGODB_URI=your_mongodb_connection_string
NASA_API_KEY=your_nasa_api_key

