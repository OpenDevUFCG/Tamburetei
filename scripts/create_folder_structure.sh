#!/bin/bash

GREEN="\e[1;32m"
BLUE="\e[1;34m"
HEAVY_MARK_EMOJI="\342\234\224"

printf "> Disciplina: ${BLUE}"
read subject

CREATE_FOLDERS="mkdir -p $subject/leites $subject/implementacoes $subject/resumos"
CHANGE_TO_DIR="cd $subject" 
CREATE_FILES="touch extras.md dificuldadesComuns.md linksUteis.md visaoGeralEDicas.md"
SHOW_DIR="tree $suject"

$CREATE_FOLDERS && $CHANGE_TO_DIR && $CREATE_FILES && $SHOW_DIR

printf "${GREEN}${HEAVY_MARK_EMOJI} Criado!\n"