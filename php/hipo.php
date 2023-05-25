<?php

$co = $argv[1];
$ca = $argv[2];

$ho = (pow($ca, 2))+(pow($co, 2));

$hi = sqrt($ho);

echo ("sua hipotenusa é igual a ". $hi);
