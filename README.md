### Установка python на ubuntu:

## Устанавливаем pyenv:

```bash
sudo apt-get install -y make build-essential git libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev
```

```bash
curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
```
```bash
nano ~/.bash_profile
```

Добавляем следующие строки в конец файла, здесь мы должны заменить «USER» на ваше системное имя пользователя

```bash
export PATH="/home/USER/.pyenv/bin:$PATH"
 
eval "$(pyenv init -)"
 
eval "$(pyenv virtualenv-init -)"
```

Cохраняем изменения с помощью Ctrl + O и выходим из nano с помощью Ctrl + X, теперь мы должны сделать эти изменения действительными, выполнив следующую команду:

```bash
source ~/.bash_profile
```
Pyenv готов к использованию.


Установиливаем любую из доступных версий:

```bash
pyenv install 3.11.3
```


## Устанавливаем poetry:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
Определите путь к каталогу, в котором установлена poetry obолочка. Этот путь зависит от вашей платформы:
На Unix/Linux: ```$HOME/.local/bin```

Проверьте, существует ли указанный каталог в вашем переменной среды PATH. PATH-это список каталогов, в которых система ищет исполняемые файлы при вводе команды в командной строке.

Если указанный каталог отсутствует в вашей переменной среды PATH, вам нужно добавить его:

Откройте файл ```~/.bashrc или ~/.bash_profile``` (в зависимости от вашей ОС и конфигурации) в редакторе текста и добавьте следующую строку в конец файла: ```export PATH=$PATH:path/to/poetry``` Сохраните файл и перезапустите терминал.

После этих шагов poetryдолжен быть доступен в вашей командной строке или терминале, и вы сможете вызывать его, используя команду:


```bash
poetry --version
```
## Настройка конфига poetry

```bash
poetry self update
```
```bash
poetry completions bash >> ~/.bash_completion
```
```bash
poetry config virtualenvs.in-project true
```
Чтобы установить нужную версию python в локальное окружение проекта используем:

```bash
pyenv local 3.11.3
```

Находим путь до бинарного файла python

```bash
pyenv which python
```

```bash
poetry env use [путь до бинарного файла python из pyenv]
```

## клонируем проект на локальный компьютер:

```bash
git clone https://github.com/SergeiNaum/novoross_society.git
```
## Переходим в директорию с проектом

```bash
cd path/to/project(novoross_society)
```

## Устанавливаем зависимости:

```bash
poetry install или make install
```

## Запускаем локальный сервер разработки

```bash
python manage.py runserver или make dev
```
сайт будет доступен по адресу: http://127.0.0.1:8000/
