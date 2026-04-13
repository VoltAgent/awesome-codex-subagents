<a href="https://github.com/VoltAgent/voltagent">
    <img width="1500" height="500" alt="codex" src="https://github.com/user-attachments/assets/35f56654-e3e7-4023-a7d5-acd5215455de" />
</a>

<br />
<br />

<div align="center">
    <strong>The awesome collection of 136+ Codex subagents across 10 categories.</strong>
    <br />
    <br />
</div>

   
<div align="center">
    
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Subagent Count](https://img.shields.io/badge/subagents-136-blue?style=classic)
[![Last Update](https://img.shields.io/github/last-commit/VoltAgent/awesome-codex-subagents?label=Last%20update&style=classic)](https://github.com/VoltAgent/awesome-codex-subagents)
[![Discord](https://img.shields.io/discord/1361559153780195478.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://s.voltagent.dev/discord)

<br />


<div align="center">
    <strong>More awesome collections for developers</strong>
    <br />
    <br />
</div>

[![Agent Skills](https://img.shields.io/static/v1?label=%E2%9A%A1%20Agent&message=Skills%2012k&color=black&style=classic)](https://github.com/VoltAgent/awesome-agent-skills)
[![Claude Code Subagents](https://img.shields.io/static/v1?label=Claude&message=Code%20Subagents%2014k&color=D97757&style=classic&logo=claude&logoColor=D97757)](https://github.com/VoltAgent/awesome-claude-code-subagents)
[![OpenClaw Skills](https://img.shields.io/static/v1?label=%F0%9F%A6%9E%20OpenClaw&message=Skills%2040k&color=f53e36&style=classic)](https://github.com/VoltAgent/awesome-openclaw-skills)
[![AI Agent Papers](https://img.shields.io/static/v1?label=arxiv&message=Agent%20Papers%20328&color=b31b1b&style=classic&logo=arxiv)](https://github.com/VoltAgent/awesome-ai-agent-papers)
</div>


# Awesome Codex Subagents

This repository serves as the definitive collection of [Codex Subagents](https://developers.openai.com/codex/subagents), specialized AI assistants designed for specific development tasks. Written specifically for Codex and aligned with the official docs.

## Installation

Use Codex custom agent directories exactly as documented:

- `~/.codex/agents/` for global agents (available in all projects)
- `.codex/agents/` for project-specific agents (higher precedence in that repo)

1. Clone this repository.
2. Copy the `.toml` agent files you want into one of the directories above.
3. Restart or refresh your Codex session if needed.
4. Delegate explicitly in prompts (Codex does not auto-spawn custom subagents).

Examples:
```bash
mkdir -p ~/.codex/agents
cp categories/01-core-development/backend-developer.toml ~/.codex/agents/
```

```bash
mkdir -p .codex/agents
cp categories/04-quality-security/reviewer.toml .codex/agents/
```

If you use agent configuration in Codex, keep it in `.codex/config.toml` under `[agents]` as described in the official docs.


### Subagent Storage Locations

| Type | Path | Availability | Precedence |
|------|------|--------------|------------|
| Project Subagents | `.codex/agents/` | Current project only | Higher |
| Global Subagents | `~/.codex/agents/` | All projects | Lower |

Note: When naming conflicts occur, project-specific subagents override global ones.


## Subagent Structure

Each subagent uses a Codex-native `.toml` format:

```toml
name = "subagent-name"
description = "When this agent should be invoked"
model = "gpt-5.3-codex-spark"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"

[instructions]
text = """
You are a [role description and expertise areas]...

[Agent-specific checklists, patterns, and guidelines]...
"""
```

### Smart Model Routing

Each subagent includes a `model` field that automatically routes it to the right model -- balancing quality and cost:

| Model | When It's Used | Examples |
|-------|----------------|----------|
| `gpt-5.4` | Deep reasoning -- architecture reviews, security audits, financial logic | `security-auditor`, `architect-reviewer`, `fintech-engineer` |
| `gpt-5.3-codex-spark` | Fast scanning, synthesis, and lighter research tasks | `search-specialist`, `docs-researcher`, `agent-installer` |

### Sandbox Mode Philosophy

Each subagent's `sandbox_mode` field controls filesystem access:
- **Read-only agents** (reviewers, auditors): `sandbox_mode = "read-only"` - analyze without modifying
- **Workspace-write agents** (developers, engineers): `sandbox_mode = "workspace-write"` - create and modify files


## Categories

### [01. Core Development](categories/01-core-development/)

Essential development subagents for everyday coding tasks.

- [**api-designer**](categories/01-core-development/api-designer.toml) - REST and GraphQL API architect
- [**backend-developer**](categories/01-core-development/backend-developer.toml) - Server-side expert for scalable APIs
- [**code-mapper**](categories/01-core-development/code-mapper.toml) - Code path mapping and ownership boundary analysis
- [**electron-pro**](categories/01-core-development/electron-pro.toml) - Desktop application expert
- [**frontend-developer**](categories/01-core-development/frontend-developer.toml) - UI/UX specialist for React, Vue, and Angular
- [**fullstack-developer**](categories/01-core-development/fullstack-developer.toml) - End-to-end feature development
- [**graphql-architect**](categories/01-core-development/graphql-architect.toml) - GraphQL schema and federation expert
- [**microservices-architect**](categories/01-core-development/microservices-architect.toml) - Distributed systems designer
- [**mobile-developer**](categories/01-core-development/mobile-developer.toml) - Cross-platform mobile specialist
- [**ui-designer**](categories/01-core-development/ui-designer.toml) - Visual design and interaction specialist
- [**ui-fixer**](categories/01-core-development/ui-fixer.toml) - Smallest safe patch for reproduced UI issues
- [**websocket-engineer**](categories/01-core-development/websocket-engineer.toml) - Real-time communication specialist

### [02. Language Specialists](categories/02-language-specialists/)

Language-specific experts with deep framework knowledge.
- [**angular-architect**](categories/02-language-specialists/angular-architect.toml) - Angular 15+ enterprise patterns expert
- [**cpp-pro**](categories/02-language-specialists/cpp-pro.toml) - C++ performance expert
- [**csharp-developer**](categories/02-language-specialists/csharp-developer.toml) - .NET ecosystem specialist
- [**django-developer**](categories/02-language-specialists/django-developer.toml) - Django 4+ web development expert
- [**dotnet-core-expert**](categories/02-language-specialists/dotnet-core-expert.toml) - .NET 8 cross-platform specialist
- [**dotnet-framework-4.8-expert**](categories/02-language-specialists/dotnet-framework-4.8-expert.toml) - .NET Framework legacy enterprise specialist
- [**elixir-expert**](categories/02-language-specialists/elixir-expert.toml) - Elixir and OTP fault-tolerant systems expert
- [**erlang-expert**](categories/02-language-specialists/erlang-expert.toml) - Erlang/OTP and rebar3 engineering expert
- [**flutter-expert**](categories/02-language-specialists/flutter-expert.toml) - Flutter 3+ cross-platform mobile expert
- [**golang-pro**](categories/02-language-specialists/golang-pro.toml) - Go concurrency specialist
- [**java-architect**](categories/02-language-specialists/java-architect.toml) - Enterprise Java expert
- [**javascript-pro**](categories/02-language-specialists/javascript-pro.toml) - JavaScript development expert
- [**kotlin-specialist**](categories/02-language-specialists/kotlin-specialist.toml) - Modern JVM language expert
- [**laravel-specialist**](categories/02-language-specialists/laravel-specialist.toml) - Laravel 10+ PHP framework expert
- [**nextjs-developer**](categories/02-language-specialists/nextjs-developer.toml) - Next.js 14+ full-stack specialist
- [**php-pro**](categories/02-language-specialists/php-pro.toml) - PHP web development expert
- [**powershell-5.1-expert**](categories/02-language-specialists/powershell-5.1-expert.toml) - Windows PowerShell 5.1 and full .NET Framework automation specialist
- [**powershell-7-expert**](categories/02-language-specialists/powershell-7-expert.toml) - Cross-platform PowerShell 7+ automation and modern .NET specialist
- [**python-pro**](categories/02-language-specialists/python-pro.toml) - Python ecosystem master
- [**rails-expert**](categories/02-language-specialists/rails-expert.toml) - Rails 8.1 rapid development expert
- [**react-specialist**](categories/02-language-specialists/react-specialist.toml) - React 18+ modern patterns expert
- [**rust-engineer**](categories/02-language-specialists/rust-engineer.toml) - Systems programming expert
- [**spring-boot-engineer**](categories/02-language-specialists/spring-boot-engineer.toml) - Spring Boot 3+ microservices expert
- [**sql-pro**](categories/02-language-specialists/sql-pro.toml) - Database query expert
- [**swift-expert**](categories/02-language-specialists/swift-expert.toml) - iOS and macOS specialist
- [**typescript-pro**](categories/02-language-specialists/typescript-pro.toml) - TypeScript specialist
- [**vue-expert**](categories/02-language-specialists/vue-expert.toml) - Vue 3 Composition API expert


### [03. Infrastructure](categories/03-infrastructure/)

DevOps, cloud, and deployment specialists.

- [**azure-infra-engineer**](categories/03-infrastructure/azure-infra-engineer.toml) - Azure infrastructure and Az PowerShell automation expert
- [**cloud-architect**](categories/03-infrastructure/cloud-architect.toml) - AWS/GCP/Azure specialist
- [**database-administrator**](categories/03-infrastructure/database-administrator.toml) - Database management expert
- [**deployment-engineer**](categories/03-infrastructure/deployment-engineer.toml) - Deployment automation specialist
- [**devops-engineer**](categories/03-infrastructure/devops-engineer.toml) - CI/CD and automation expert
- [**devops-incident-responder**](categories/03-infrastructure/devops-incident-responder.toml) - DevOps incident management
- [**docker-expert**](categories/03-infrastructure/docker-expert.toml) - Docker containerization and optimization expert
- [**incident-responder**](categories/03-infrastructure/incident-responder.toml) - System incident response expert
- [**kubernetes-specialist**](categories/03-infrastructure/kubernetes-specialist.toml) - Container orchestration master
- [**network-engineer**](categories/03-infrastructure/network-engineer.toml) - Network infrastructure specialist
- [**platform-engineer**](categories/03-infrastructure/platform-engineer.toml) - Platform architecture expert
- [**security-engineer**](categories/03-infrastructure/security-engineer.toml) - Infrastructure security specialist
- [**sre-engineer**](categories/03-infrastructure/sre-engineer.toml) - Site reliability engineering expert
- [**terraform-engineer**](categories/03-infrastructure/terraform-engineer.toml) - Infrastructure as Code expert
- [**terragrunt-expert**](categories/03-infrastructure/terragrunt-expert.toml) - Terragrunt orchestration and DRY IaC specialist
- [**windows-infra-admin**](categories/03-infrastructure/windows-infra-admin.toml) - Active Directory, DNS, DHCP, and GPO automation specialist

<details>
<summary><b>04. Quality & Security</b> — Testing, security, and code quality experts (16 agents)</summary>

### [04. Quality & Security](categories/04-quality-security/)

- [**accessibility-tester**](categories/04-quality-security/accessibility-tester.toml) - A11y compliance expert
- [**ad-security-reviewer**](categories/04-quality-security/ad-security-reviewer.toml) - Active Directory security and GPO audit specialist
- [**architect-reviewer**](categories/04-quality-security/architect-reviewer.toml) - Architecture review specialist
- [**browser-debugger**](categories/04-quality-security/browser-debugger.toml) - Browser-based reproduction and client-side debugging
- [**chaos-engineer**](categories/04-quality-security/chaos-engineer.toml) - System resilience testing expert
- [**code-reviewer**](categories/04-quality-security/code-reviewer.toml) - Code quality guardian
- [**compliance-auditor**](categories/04-quality-security/compliance-auditor.toml) - Regulatory compliance expert
- [**debugger**](categories/04-quality-security/debugger.toml) - Advanced debugging specialist
- [**error-detective**](categories/04-quality-security/error-detective.toml) - Error analysis and resolution expert
- [**penetration-tester**](categories/04-quality-security/penetration-tester.toml) - Ethical hacking specialist
- [**performance-engineer**](categories/04-quality-security/performance-engineer.toml) - Performance optimization expert
- [**powershell-security-hardening**](categories/04-quality-security/powershell-security-hardening.toml) - PowerShell security hardening and compliance specialist
- [**qa-expert**](categories/04-quality-security/qa-expert.toml) - Test automation specialist
- [**reviewer**](categories/04-quality-security/reviewer.toml) - PR-style review for correctness, security, and regressions
- [**security-auditor**](categories/04-quality-security/security-auditor.toml) - Security vulnerability expert
- [**test-automator**](categories/04-quality-security/test-automator.toml) - Test automation framework expert

</details>

<details>
<summary><b>05. Data & AI</b> — Data engineering, ML, and AI specialists (12 agents)</summary>

### [05. Data & AI](categories/05-data-ai/)

- [**ai-engineer**](categories/05-data-ai/ai-engineer.toml) - AI system design and deployment expert
- [**data-analyst**](categories/05-data-ai/data-analyst.toml) - Data insights and visualization specialist
- [**data-engineer**](categories/05-data-ai/data-engineer.toml) - Data pipeline architect
- [**data-scientist**](categories/05-data-ai/data-scientist.toml) - Analytics and insights expert
- [**database-optimizer**](categories/05-data-ai/database-optimizer.toml) - Database performance specialist
- [**llm-architect**](categories/05-data-ai/llm-architect.toml) - Large language model architect
- [**machine-learning-engineer**](categories/05-data-ai/machine-learning-engineer.toml) - Machine learning systems expert
- [**ml-engineer**](categories/05-data-ai/ml-engineer.toml) - Machine learning specialist
- [**mlops-engineer**](categories/05-data-ai/mlops-engineer.toml) - MLOps and model deployment expert
- [**nlp-engineer**](categories/05-data-ai/nlp-engineer.toml) - Natural language processing expert
- [**postgres-pro**](categories/05-data-ai/postgres-pro.toml) - PostgreSQL database expert
- [**prompt-engineer**](categories/05-data-ai/prompt-engineer.toml) - Prompt optimization specialist
- [**market-analyst**](categories/05-data-ai/market-analyst.toml) - Stock/crypto market analysis with news bias scoring via Helium MCP

</details>

<details>
<summary><b>06. Developer Experience</b> — Tooling and developer productivity experts (13 agents)</summary>

### [06. Developer Experience](categories/06-developer-experience/)

- [**build-engineer**](categories/06-developer-experience/build-engineer.toml) - Build system specialist
- [**cli-developer**](categories/06-developer-experience/cli-developer.toml) - Command-line tool creator
- [**dependency-manager**](categories/06-developer-experience/dependency-manager.toml) - Package and dependency specialist
- [**documentation-engineer**](categories/06-developer-experience/documentation-engineer.toml) - Technical documentation expert
- [**dx-optimizer**](categories/06-developer-experience/dx-optimizer.toml) - Developer experience optimization specialist
- [**git-workflow-manager**](categories/06-developer-experience/git-workflow-manager.toml) - Git workflow and branching expert
- [**legacy-modernizer**](categories/06-developer-experience/legacy-modernizer.toml) - Legacy code modernization specialist
- [**mcp-developer**](categories/06-developer-experience/mcp-developer.toml) - Model Context Protocol specialist
- [**powershell-module-architect**](categories/06-developer-experience/powershell-module-architect.toml) - PowerShell module and profile architecture specialist
- [**powershell-ui-architect**](categories/06-developer-experience/powershell-ui-architect.toml) - PowerShell UI/UX specialist for WinForms, WPF, Metro frameworks, and TUIs
- [**refactoring-specialist**](categories/06-developer-experience/refactoring-specialist.toml) - Code refactoring expert
- [**slack-expert**](categories/06-developer-experience/slack-expert.toml) - Slack platform and @slack/bolt specialist
- [**tooling-engineer**](categories/06-developer-experience/tooling-engineer.toml) - Developer tooling specialist

</details>

<details>
<summary><b>07. Specialized Domains</b> — Domain-specific technology experts (12 agents)</summary>

### [07. Specialized Domains](categories/07-specialized-domains/)

- [**api-documenter**](categories/07-specialized-domains/api-documenter.toml) - API documentation specialist
- [**blockchain-developer**](categories/07-specialized-domains/blockchain-developer.toml) - Web3 and crypto specialist
- [**embedded-systems**](categories/07-specialized-domains/embedded-systems.toml) - Embedded and real-time systems expert
- [**fintech-engineer**](categories/07-specialized-domains/fintech-engineer.toml) - Financial technology specialist
- [**game-developer**](categories/07-specialized-domains/game-developer.toml) - Game development expert
- [**iot-engineer**](categories/07-specialized-domains/iot-engineer.toml) - IoT systems developer
- [**m365-admin**](categories/07-specialized-domains/m365-admin.toml) - Microsoft 365, Exchange Online, Teams, and SharePoint administration specialist
- [**mobile-app-developer**](categories/07-specialized-domains/mobile-app-developer.toml) - Mobile application specialist
- [**payment-integration**](categories/07-specialized-domains/payment-integration.toml) - Payment systems expert
- [**quant-analyst**](categories/07-specialized-domains/quant-analyst.toml) - Quantitative analysis specialist
- [**risk-manager**](categories/07-specialized-domains/risk-manager.toml) - Risk assessment and management expert
- [**seo-specialist**](categories/07-specialized-domains/seo-specialist.toml) - Search engine optimization expert

</details>

<details>
<summary><b>08. Business & Product</b> — Product management and business analysis (11 agents)</summary>

### [08. Business & Product](categories/08-business-product/)

- [**business-analyst**](categories/08-business-product/business-analyst.toml) - Requirements specialist
- [**content-marketer**](categories/08-business-product/content-marketer.toml) - Content marketing specialist
- [**customer-success-manager**](categories/08-business-product/customer-success-manager.toml) - Customer success expert
- [**legal-advisor**](categories/08-business-product/legal-advisor.toml) - Legal and compliance specialist
- [**product-manager**](categories/08-business-product/product-manager.toml) - Product strategy expert
- [**project-manager**](categories/08-business-product/project-manager.toml) - Project management specialist
- [**sales-engineer**](categories/08-business-product/sales-engineer.toml) - Technical sales expert
- [**scrum-master**](categories/08-business-product/scrum-master.toml) - Agile methodology expert
- [**technical-writer**](categories/08-business-product/technical-writer.toml) - Technical documentation specialist
- [**ux-researcher**](categories/08-business-product/ux-researcher.toml) - User research expert
- [**wordpress-master**](categories/08-business-product/wordpress-master.toml) - WordPress development and optimization expert

</details>

<details>
<summary><b>09. Meta & Orchestration</b> — Agent coordination and meta-programming (12 agents)</summary>

### [09. Meta & Orchestration](categories/09-meta-orchestration/)

- [**agent-installer**](categories/09-meta-orchestration/agent-installer.toml) - Browse and install agents from this repository via GitHub
- [**agent-organizer**](categories/09-meta-orchestration/agent-organizer.toml) - Multi-agent coordinator
- [**context-manager**](categories/09-meta-orchestration/context-manager.toml) - Context optimization expert
- [**error-coordinator**](categories/09-meta-orchestration/error-coordinator.toml) - Error handling and recovery specialist
- [**it-ops-orchestrator**](categories/09-meta-orchestration/it-ops-orchestrator.toml) - IT operations workflow orchestration specialist
- [**knowledge-synthesizer**](categories/09-meta-orchestration/knowledge-synthesizer.toml) - Knowledge aggregation expert
- [**multi-agent-coordinator**](categories/09-meta-orchestration/multi-agent-coordinator.toml) - Advanced multi-agent orchestration
- [**performance-monitor**](categories/09-meta-orchestration/performance-monitor.toml) - Agent performance optimization
- [**pied-piper**](https://github.com/sathish316/pied-piper/) - Orchestrate Team of AI Subagents for repetitive SDLC workflows
- [**task-distributor**](categories/09-meta-orchestration/task-distributor.toml) - Task allocation specialist
- [**workflow-orchestrator**](categories/09-meta-orchestration/workflow-orchestrator.toml) - Complex workflow automation

</details>

<details>
<summary><b>10. Research & Analysis</b> — Research, search, and analysis specialists (7 agents)</summary>

### [10. Research & Analysis](categories/10-research-analysis/)

- [**competitive-analyst**](categories/10-research-analysis/competitive-analyst.toml) - Competitive intelligence specialist
- [**data-researcher**](categories/10-research-analysis/data-researcher.toml) - Data discovery and analysis expert
- [**docs-researcher**](categories/10-research-analysis/docs-researcher.toml) - Documentation-backed API and framework verification
- [**market-researcher**](categories/10-research-analysis/market-researcher.toml) - Market analysis and consumer insights
- [**research-analyst**](categories/10-research-analysis/research-analyst.toml) - Comprehensive research specialist
- [**search-specialist**](categories/10-research-analysis/search-specialist.toml) - Advanced information retrieval expert
- [**trend-analyst**](categories/10-research-analysis/trend-analyst.toml) - Emerging trends and forecasting expert

</details>

## Understanding Subagents

Subagents are specialized AI assistants that enhance Codex's capabilities by providing task-specific expertise. They act as dedicated helpers that Codex can call upon when encountering particular types of work.

### What Makes Subagents Special?

**Independent Context Windows**
Every subagent operates within its own isolated context space, preventing cross-contamination between different tasks and maintaining clarity in the primary conversation thread.

**Domain-Specific Intelligence**
Subagents come equipped with carefully crafted instructions tailored to their area of expertise, resulting in superior performance on specialized tasks.

**Shared Across Projects**
After creating a subagent, you can utilize it throughout various projects and distribute it among team members to ensure consistent development practices.

**Explicit Delegation**
Codex does not spawn subagents automatically. Use explicit delegation prompts to specify which agents to spawn, how to divide the work, and what shape the result should take.

### Core Advantages

- **Memory Efficiency**: Isolated contexts prevent the main conversation from becoming cluttered with task-specific details
- **Enhanced Accuracy**: Specialized prompts and configurations lead to better results in specific domains
- **Workflow Consistency**: Team-wide subagent sharing ensures uniform approaches to common tasks
- **Codex-Native**: Uses `.toml` agent files aligned with official Codex subagent docs

### Example Workflows

**PR review workflow:**
```text
Review this branch with parallel subagents. Have reviewer look for correctness, security, and missing tests. Have docs_researcher verify the framework APIs this patch depends on. Wait for both and summarize the findings with file references.
```

**Bug investigation workflow:**
```text
Investigate the broken settings flow. Have code_mapper trace the owning code paths, browser_debugger reproduce the bug in the browser, and frontend_developer propose the smallest fix after the failure is understood. Wait for the read-heavy agents first, then continue.
```

**Repo exploration and planning workflow:**
```text
Use search_specialist to locate the code related to payment retries, knowledge_synthesizer to summarize the current design, and refactoring_specialist to propose a minimal refactor plan. Return a concrete action list.
```
## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

- Submit new subagents via PR
- Improve existing definitions
- Report issues and bugs


## License

MIT License - see [LICENSE](LICENSE)

This repository is a curated collection of subagent definitions contributed by both the maintainers and the community. All subagents are provided "as is" without warranty. We do not audit or guarantee the security or correctness of any subagent. Review before use, the maintainers accept no liability for any issues arising from their use.

If you find an issue with a listed subagent or want your contribution removed, please open an issue in this repository and we'll address it promptly.
