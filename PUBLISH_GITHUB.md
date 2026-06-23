# Publicacao no GitHub

## 1. Inicializar repositorio local

```powershell
git init
git branch -M main
```

## 2. Adicionar arquivos e criar commit

```powershell
git add .
git commit -m "Entrega automacao Python Selenium Behave"
```

## 3. Criar repositorio remoto no GitHub

Crie um repositorio vazio no GitHub, por exemplo: `python-automation-run`.

## 4. Vincular remoto e enviar

Substitua `SEU_USUARIO` e `SEU_REPO`:

```powershell
git remote add origin https://github.com/SEU_USUARIO/SEU_REPO.git
git push -u origin main
```

## 5. Confirmar publicacao

Verifique no GitHub se os arquivos principais estao presentes:

- `README.md`
- `RELATORIO_ENTREGA.md`
- `features/`
- `pages/`
- `utils/`
- `requirements.txt`
