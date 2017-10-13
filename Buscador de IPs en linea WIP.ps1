"#"
"#"
"#"
"#"
"#"
"#"
"#"
"#"
"#"
"#"

$red    = Read-Host -Prompt "Ingresar IP con formato 10.xxx.xxx: "
$inicio = Read-Host -Prompt "Ingresar IP inicial: "
$fin    = Read-Host -Prompt "Ingresar IP final: "

$rango = $inicio..$fin

Foreach ($octeto in $rango) 
{

if (Test-NetConnection $red`.$octeto -InformationLevel quiet){

    "$red`.$octeto"
    #"$red.$octeto" | Out-File -FilePath C:\db\equipos_live$red.csv -Append -Force
    }

}

pause

