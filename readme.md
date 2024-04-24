# 🚀 Curso Odoo

Bienvenidos al curso de odoo desde cero

## 🕹️ Instaladores

Acorde al tipo de sistema operativo se recomienda instalar

- [Docker Windows](https://www.docker.com/products/docker-desktop/)

- [Pycharn](https://www.jetbrains.com/pycharm/) [Windows,Mac, Linux]

- [Postgres](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) [Windows]

- [dbeaver](https://dbeaver.io/) _para gestionar la Base de Datos_

- [VSCode](https://code.visualstudio.com/)

- [Python](https://www.python.org/downloads/)

- [Git](https://git-scm.com/)

## 😎 Instalación

### Método 1

1. Creamos un directorio
2. Descargamos el proyecto de odoo directamente del repositorio para ello ocupamos el siguiente comando

   ```bash
   git clone -b 16.0 --depth 1 https://github.com/odoo/odoo.git odoo
   ```

3. Instalamos python
4. Sobre el directorio creamos un **entorno virtual** para python con el siguiente comando
   ```bash
   pip install virtualenv
   python -m venv <name_enviroment>
   source <name_enviroment>/bin/activate # Linux
   source <name_enviroment>/Script/activate # Windowns
   ```
5. Sobre el directorio ejecutamos el siguiente comando
   ```bash
   pip install -r requiremenst.txt
   ```
   esto les permitira instalar todas las dependencias de odoo necesarias para correr el proyecto.
6. Crear un archivo **odoo.conf**
   ```
   [options]
   addons_path = [<directory_addons>, ]
   data_dir = /var/lib/odoo
   admin_passwd = 1234
   limit_time_cpu = 6000
   limit_time_real = 12000
   proxy_mode = 1
   db_maxconn=1000
   db_host = <db_host>
   db_maxconn = 64
   db_name = False
   db_user = odoo
   db_password = <db_password>
   db_port = 5432
   db_sslmode = prefer
   db_template = template0
   http_port = 8069
   ```
7. Para correr odoo necesitamos el siguientes comando desde la consola
   ```bash
   python odoo/odoo-bin -c odoo.conf --dev all
   ```
8. Si no les da problemas y levanta el proyecto terminamos con la instalación podemos empezar a probar odoo 🚀😎.
9. En un navegador colocar `http://localhost:8069` o en el puerto que configuraron en el **odoo.conf**

> **NOTA:** En windows en caso de requerir instalar lo siguiente

```bash
pip install pypiwin32
pip install pyOpenSSL
```

### 🕹️ Metodo 2

Para el despliegue necesitaremos **docker** el cual nos permitirá hacer la instalación más directa ya que trae configurado todos los pasos previos anteriormente Linux, Mac o Windows.

1. Para **Linux** deberan instalar **docker** en caso de Windows el instalador lo pueden encontrar en la sección de instaladores
2. Instalación Docker en Linux
   - [Debian](https://docs.docker.com/engine/install/debian/)
   - [Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
3. Docker compose
   - [Docker compose](https://docs.docker.com/compose/install/linux/)
4. Una vez instalado ejecutamos el siguiente comando en el directorio ya esta configurado para que pueden empezar a usar

   ```bash
   # acorde a la version del compose puede ser diferente la ejecución
   1. docker-compose up -d --build
   2. docker compose up -d
   ```

## 🙊 Odoo VSCode

Mencionar que deben seguir el **método 1**

### Extensiones

- [Odoo Code Snippets](https://marketplace.visualstudio.com/items?itemName=mstuttgart.odoo-snippets)
- [Odoo IDE](https://marketplace.visualstudio.com/items?itemName=trinhanhngoc.vscode-odoo)

### Launch para ejecutar odoo desde VSCode

Deben tener odoo en el directorio para la parte de args pueden seguir agregando configuraciones acorde a su requerimiento.

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Odoo Run",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/odoo/odoo-bin",
      "console": "integratedTerminal",
      "args": ["--config=${workspaceFolder}/config/odoo.conf", "-d db_test"]
    }
  ]
}
```
