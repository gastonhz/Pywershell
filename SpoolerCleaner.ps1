#github.com/gastonhz/Pywershell
"Este script busca las PCs en red dentro de un rango determinado y les borra la cola de impresión."
" "
##Esta parte releva las PCs conectadas y las tira en un csv 
$red    = Read-Host -Prompt "Ingresar IP con formato 10.xxx.xxx: "
$inicio = Read-Host -Prompt "Ingresar IP inicial: "
$fin    = Read-Host -Prompt "Ingresar IP final: "

$rango = $inicio..$fin

Foreach ($octeto in $rango) 
{

if (Test-NetConnection $red`.$octeto -InformationLevel quiet){
    "$red.$octeto" | Out-File -FilePath C:\db\equipos_live$red.csv -Append -Force
    }
}
"Relevamiento de equipos en red finalizado, se adjuntó resultado a C:\db\equipos_live$red.csv"

####Acá empieza a limpiar las PCs tomandolas del csv
$plataformas = Get-Content C:\db\equipos_live$red.csv

Foreach ($pcsuc in $plataformas)

{
Get-Service -ComputerName $pcsuc -Name spooler | Stop-Service
"Deteniendo servicio spooler en "+$pcsuc
}

Foreach ($pcsuc in $plataformas)

{
Remove-Item -path \\$pcsuc\c$\Windows\System32\spool\PRINTERS\* -force
"Borrando cola de impresión en "+$pcsuc
}

Foreach ($pcsuc in $plataformas)

{
Get-Service -ComputerName $pcsuc -Name spooler | Start-Service
"Iniciando servicio spooler en "+$pcsuc
}

pause
