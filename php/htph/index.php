<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    

    <form name="form" action="" method="get">
    <input name="input1" type="text" placeholder="Dá teu input ae" value=""></input>
    <input type="submit" value="Submit"></input>
    </form>
    <span class="texto php" placeholder="Seu input"><?php $varx = "";$varx = $_GET['input1'];if($varx == 'Você não digitou nada'){echo("Engraçadinho né");} elseif ($varx != ""){echo("Seu input: '". $varx. "'");} elseif($varx == ''){echo("Você não digitou nada");}?></span>
</body>
</html>