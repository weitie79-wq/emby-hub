# emby-hub

Emb y 管理面板（Emby Hub）

简介
- 多实例 Emby 管理面板（MVP scaffold）
- 技术栈：FastAPI（后端） + React + Vite + Ant Design（前端）
- 数据库：Postgres
- 异步任务：Celery + Redis
- 部署：Docker Compose

快速开始（开发）

1. 复制 .env.example 为 .env 并填写配置
2. 启动服务：
   docker-compose up --build

后端 API： http://localhost:8000
前端： http://localhost:3000

更多文档见 ./backend 与 ./frontend 目录
