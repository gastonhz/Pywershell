#Este script toma un rango de IPs introducido por el usuario y verifica su estado, si responden a red las imprime en pantalla.
#github.com/gastonhz/Pywershell
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
$inicio = Read-Host -Prompt "Último octeto inicial: "
$fin    = Read-Host -Prompt "Último octeto final: "

$rango = $inicio..$fin

Foreach ($octeto in $rango) 
{

if (Test-NetConnection $red`.$octeto -InformationLevel quiet){

    "$red`.$octeto"
    #"$red.$octeto" | Out-File -FilePath C:\db\equipos_live$red.csv -Append -Force
    }

}

pause
