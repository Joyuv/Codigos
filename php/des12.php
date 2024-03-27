<?php

$preco = readline("Insira o valor do preço: ");

$des = readline("Insira o valor do desconto: ");

$pf = ($preco - ($preco * ($des / 100)));

var_dump("O valor final do produto foi ". $pf. " que legal.");