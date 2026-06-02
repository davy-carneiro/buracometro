# Deploy do Buracometro na Vercel

## O que precisa criar

1. Um projeto na Vercel conectado ao repositório do GitHub.
2. Um banco Postgres online, como Neon ou Supabase.
3. Uma conta Cloudinary para salvar imagens de posts e fotos de perfil.

## Variáveis de ambiente na Vercel

Cadastre estas variáveis em Project Settings > Environment Variables:

```env
DEBUG=False
SECRET_KEY=uma-chave-secreta-grande-e-unica
ALLOWED_HOSTS=.vercel.app
CSRF_TRUSTED_ORIGINS=https://*.vercel.app
DATABASE_URL=postgres://usuario:senha@host:5432/banco
CLOUDINARY_URL=cloudinary://api_key:api_secret@cloud_name
SECURE_SSL_REDIRECT=True
SECURE_HSTS_SECONDS=0
```

Quando tiver domínio próprio, adicione ele em `ALLOWED_HOSTS` e `CSRF_TRUSTED_ORIGINS`.

## Depois do primeiro deploy

Rode as migrations no banco online:

```bash
python buracometro/manage.py migrate
```

Depois crie um admin no banco online:

```bash
python buracometro/manage.py createsuperuser
```

## Observações

- Localmente o projeto continua usando `db.sqlite3`.
- Na Vercel, o projeto usa `DATABASE_URL`.
- Uploads de imagem só ficam persistentes em produção se `CLOUDINARY_URL` estiver configurado.
- `SECURE_HSTS_SECONDS` ficou `0` por segurança. Ative apenas quando o domínio HTTPS estiver definitivo.
