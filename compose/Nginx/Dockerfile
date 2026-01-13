######################
#--STAGE 1: BUILDER--#
######################

    # 1 - importar a imagem base
FROM node:20-slim AS builder 

    # 2 - Definir o diretório em que estamos trabalhando
WORKDIR /app

    # 3 - Copiar os manifests
COPY package.json package-lock.json ./

    # 4 - Instala as dependências (Tailwind)
RUN npm ci

    # 5 - Copia o necessário (possíveis alterações)
COPY static/ ./static/ 

    # 6 - Roda o build do frontend
RUN npm run build

######################
#--STAGE 2: RUNTIME--#
######################

    # 1 - Importar a imagem base
FROM nginx:slim AS runtime

    # 2 - Copia os arquivos buildados no Node pro Nginx
COPY --from=builder /app /usr/share/nginx/html

    # 3 - Copiar os arquivos estáticos
COPY static/ /usr/share/nginx/html/static

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]