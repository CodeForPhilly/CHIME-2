##########################
### --- BASE IMAGE --- ###
##########################
ARG BASE="debian:latest"
FROM $BASE

####################
### --- META --- ####
######################
LABEL maintainer="Brian Ross <ml@brianthomasross.com>" \
        description="Dockerized chime2"

########################
### --- CONFIG --- ###
####################
# ARG is only true during build and creates no new layers
ARG USERNAME="chime_dev"
ARG USER_UID="1000"
ARG USER_GID=$USER_UID
ARG USER_DIR="/home/$USERNAME"

##################################
### --- STOP MOST WARNINGS --- ###
##################################
ARG DEBIAN_FRONTEND=noninteractive

################################
### --- ENVIRONMENT VARS --- ###
################################
# ENV persists after container build
    # PATH manipulations should go here
ENV PATH="$PATH:" \
    # Stops CPython from producing bytecode
    PYTHONDONTWRITEBYTECODE=1 \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    PORT=8000 \
    SHELL="/bin/bash"

# BETTER THAN COPY LAYERS DURING BUILD USE `git clone`
ARG REPO_URL="https://www.github.com/CodeforPhilly/CHIME-2.git"

###########################
### --- BUILD FILES --- ###
###########################
ARG BUILD_PKGS="apt-transport-https \
                bash \
                build-essential \
                bzip2 \
                ca-certificates \
                curl \
                cmake \
                g++ \
                gdebi-core \
                gfortran \
                git \
                iproute2 \
                libboost-all-dev \
                libbz2-dev \
                libcairo2 \
                libcairo2-dev \
                libdb5.3-dev \
                libeigen3-dev \
                libexpat1-dev \
                libffi-dev \
                libgfortran3 \
                libgcc1 \
                libgdbm-dev \
                liblzma-dev \
                libncurses5-dev \
                libncursesw5-dev \
                libreadline-dev \
                libsm6 \
                libssl-dev \
                libsqlite3-dev \
                libxext-dev \
                libxrender1 \
                lmodern \
                locales \
                lsb-base \
                net-tools \
                network-manager \
                lsb-core \
                patch \
                python3-dev \
                python3-venv \
                run-one \
                software-properties-common \
                sudo \
                tk-dev \
                wget \
                unzip \
                zlib1g-dev"

# SET ROOT USER EXPLICITLY
USER root

# BEGIN BUILD
RUN apt-get update --fix-missing \
    && apt-get upgrade -yq \
    && echo "BEGIN INSTALL APT-GET PACKAGES"
    && apt-get install -yq \
    # Packages here should be places in alphabetical order
    $BUILD_PKGS \
    ###########################
    ### --- CLEAN CACHE --- ###
    ###########################
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/* \
    ######################
    ### --- PYTHON --- ###
    ######################
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt install -yq \
    $PYTHON_VERSION \
    python3-pip \
    # INSTALL DEPENDS
    && pip3 install -yq \
    $APP_DEPENDENCIES \
    ##########################################
    ### --- PASSWDLESS NOT ROOT SUDOER --- ###
    ##########################################
    && groupadd --gid $USER_GID $USERNAME \
    && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/suoders.d/$USERNAME \
    && touch $USER_DIR/.sudo_as_admin_successful \
    su -i $USERNAME \
    && cd \
    && git clone $REPO_URL

WORKDIR $USER_DIR/CHIME-2/src
EXPOSE $PORT
USER $USERNAME

CMD ["/bin/bash -c", "gunicorn dashapp:server --bind 0.0.0.0:$PORT --chdir"]




