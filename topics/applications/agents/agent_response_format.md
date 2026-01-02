# Agent Response Format

## Overview
The agent uses a standardized response format called ResponseFormatter to structure its responses to users. This ensures consistent communication and proper data handling.

## Agent Result Format
The agent must return responses in a standardized JSON format within a ```agent-result block at the end of each response. The format includes the following fields:

- `summary`: Brief description of the work performed (3-5 sentences) with HTML formatting support for Telegram
- `answer`: Response to the user's question if it was a question-based request (only filled if user asked a question)
- `created`: List of created files and folders (relative paths)
- `edited`: List of edited files and folders (relative paths) 
- `deleted`: List of deleted files and folders (relative paths)
- `links`: List of connections with other files/folders in the knowledge base with descriptions
- `insite`: Textual field containing interesting insights based on content analysis

## Available HTML Tags for Telegram
The response supports specific HTML tags for formatting:

### Text formatting:
- `<b>` or `<strong>` for bold text
- `<i>` or `<em>` for italic text
- `<u>` or `<ins>` for underlined text
- `<s>`, `<strike>`, or `<del>` for strikethrough text

### Special elements:
- `<span class="tg-spoiler">` for spoiler text
- `<blockquote>` for quotes
- `<a href="URL">` for links
- `<code>` for inline code
- `<pre>` for code blocks

## Prompt Directory Structure
The agent uses prompts stored in `/data/prompts/note_mode_v2/` with the following structure:

- `agent_mode.md` - Configuration for agent mode operation
- `note_mode.md` - Configuration for note-taking mode
- `media/` - Contains media-related instructions (`instruction_v3.md`)
- `qwen_code_cli/` - Contains CLI-specific instructions (`instruction_v4.md`)
- `response_formatter/` - Contains response formatting rules (`instruction_v1.md`)
- `shared/` - Contains shared strategies (`search_strategy_v1.md`)

## Important Rules:
- Always return results in the specified JSON format
- Fill all fields even if empty (use empty arrays [])
- Use relative paths for all file references
- Only use supported HTML tags for formatting