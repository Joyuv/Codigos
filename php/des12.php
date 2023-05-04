<?php

$preco = readline("Insira o valor do preço: ");

$des = readline("Insira o valor do desconto: ");

$pf = ($preco * ($des / 100));

$puf = ($preco - $pf);

var_dump("O valor final do produto foi ". $puf. " que legal.");
