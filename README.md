# LLM Code Review

LLM Code Review is an AI-powered GitHub Action that automatically reviews pull requests and labels issues using large language models hosted on Groq and the RoBERTa model. This tool helps open source maintainers manage their repositories more efficiently by providing automated code reviews and issue labeling.

## Features

- Automated code reviews for pull requests using Groq's powerful language models for code analysis
- Automatic issue labeling using RoBERTa model for issue classification

## Setup

Follow these steps to set up LLM Code Review in your repository:

### 1. Obtain a Groq API Key and set it as a GitHub Secret

1. Visit the [Groq website](https://console.groq.com) and sign up for an account.
2. Navigate to groq account settings or API section to generate a new API key.
3. In your GitHub repository, go to "Settings" > "Secrets and variables" > "Actions".
4. Click on "New repository secret".
5. Name the secret `GROQ_API_KEY` and paste your Groq API key as the value.

### 2. Create a GitHub Actions Workflow

1. In your repository, create a `.github/workflows` directory if it doesn't already exist.
2. Create a new file in this directory, e.g., `llm-code-review.yml`.
3. Copy and paste the following YAML content into the file:
```yaml
name: AI Code Review

on:
  pull_request:
    types: [opened, synchronize, reopened]
  issues:
    types: [opened, reopened]

jobs:
  repofix:
    runs-on: ubuntu-latest
    steps:
      - name: Run RepoFixAI
        uses: Manav916/llm-code-review@main
        with:
          groq_api_key: ${{ secrets.GROQ_API_KEY }}
          groq_model: 'llama3-70b-8192'
          github_token: ${{ secrets.GITHUB_TOKEN }}
          # exclude_extensions: 'txt'
          repo_owner: ${{ github.repository_owner }}
          repo_name: ${{ github.event.repository.name }}
          event_number: ${{ github.event.number || github.event.issue.number }} # when listening for both pull requests and issues
          event_name: ${{ github.event_name }}
```
4. Commit the file to your repository.
5. Make sure to give read and write permissions to your workflows in settings.

With these steps completed, LLM Code Review will automatically run on new pull requests and issues in your repository.

## Configuration

You can customize the behavior of LLM Code Review by modifying the workflow file:

- `groq_model`: Specify the Groq model to use for code review.
- `exclude_extensions`: Uncomment and modify to exclude specific file types from review.

## Contributing

Contributions to LLM Code Review are welcome! Please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
