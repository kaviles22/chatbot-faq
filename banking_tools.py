from langchain.tools import BaseTool
from typing import Optional, Dict, Any
from datetime import datetime, timedelta
import random

class SaldoCuentaTool(BaseTool):
    name: str = "saldo_cuenta"
    description: str = "Obtiene el saldo actual de la cuenta bancaria del cliente"
    
    def _run(self, query: str = "") -> str:
        # Simulación de datos - en producción esto consultaría la base de datos real
        saldo = random.uniform(500, 5000)
        return f"Su saldo actual es de ${saldo:.2f} USD"
    
    def _arun(self, query: str):
        raise NotImplementedError("Este tool no soporta ejecución asíncrona")

class InfoTarjetaCreditoTool(BaseTool):
    name: str = "info_tarjeta_credito"
    description: str = "Obtiene información de la tarjeta de crédito: mínimo a pagar, total a pagar, fecha próxima de pago y fecha de corte"
    
    def _run(self, query: str = "") -> str:
        # Simulación de datos
        total_pagar = random.uniform(200, 2000)
        minimo_pagar = total_pagar * 0.05  # 5% del total
        
        # Fechas simuladas
        fecha_corte = datetime.now().replace(day=15)
        if fecha_corte < datetime.now():
            fecha_corte = fecha_corte.replace(month=fecha_corte.month + 1 if fecha_corte.month < 12 else 1)
        
        fecha_pago = fecha_corte + timedelta(days=20)
        
        return f"""Información de su tarjeta de crédito:
- Total a pagar: ${total_pagar:.2f} USD
- Mínimo a pagar: ${minimo_pagar:.2f} USD
- Fecha de corte: {fecha_corte.strftime('%d/%m/%Y')}
- Fecha próxima de pago: {fecha_pago.strftime('%d/%m/%Y')}"""
    
    def _arun(self, query: str):
        raise NotImplementedError("Este tool no soporta ejecución asíncrona")

class CreditoBancarioTool(BaseTool):
    name: str = "credito_bancario"
    description: str = "Obtiene información del crédito bancario: valor total, valor ya pagado y fecha próxima de pago"
    
    def _run(self, query: str = "") -> str:
        # Simulación de datos
        valor_total = random.uniform(10000, 50000)
        valor_pagado = random.uniform(2000, valor_total * 0.8)
        valor_pendiente = valor_total - valor_pagado
        
        # Fecha próxima de pago (próximo día 10)
        proxima_fecha = datetime.now().replace(day=10)
        if proxima_fecha < datetime.now():
            if proxima_fecha.month == 12:
                proxima_fecha = proxima_fecha.replace(year=proxima_fecha.year + 1, month=1)
            else:
                proxima_fecha = proxima_fecha.replace(month=proxima_fecha.month + 1)
        
        return f"""Información de su crédito bancario:
- Valor total del crédito: ${valor_total:.2f} USD
- Valor ya pagado: ${valor_pagado:.2f} USD
- Valor pendiente: ${valor_pendiente:.2f} USD
- Fecha próxima de pago: {proxima_fecha.strftime('%d/%m/%Y')}"""
    
    def _arun(self, query: str):
        raise NotImplementedError("Este tool no soporta ejecución asíncrona")

class PolizasTool(BaseTool):
    name: str = "info_polizas"
    description: str = "Obtiene información de las pólizas de seguros del cliente: vida, vehicular, hogar, etc."
    
    def _run(self, query: str = "") -> str:
        # Simulación de datos de pólizas - en producción esto consultaría la base de datos real
        polizas_disponibles = [
            {
                "tipo": "Seguro de Vida",
                "numero": "POL-" + str(random.randint(100000, 999999)),
                "cobertura": random.uniform(50000, 200000),
                "prima_mensual": random.uniform(50, 150),
                "estado": "Activa",
                "vencimiento": (datetime.now() + timedelta(days=random.randint(30, 365))).strftime('%d/%m/%Y')
            },
            {
                "tipo": "Seguro Vehicular",
                "numero": "POL-" + str(random.randint(100000, 999999)),
                "cobertura": random.uniform(15000, 40000),
                "prima_mensual": random.uniform(80, 200),
                "estado": "Activa",
                "vencimiento": (datetime.now() + timedelta(days=random.randint(30, 365))).strftime('%d/%m/%Y')
            },
            {
                "tipo": "Seguro de Hogar",
                "numero": "POL-" + str(random.randint(100000, 999999)),
                "cobertura": random.uniform(80000, 300000),
                "prima_mensual": random.uniform(40, 120),
                "estado": "Activa",
                "vencimiento": (datetime.now() + timedelta(days=random.randint(30, 365))).strftime('%d/%m/%Y')
            }
        ]
        
        # Seleccionar 1-3 pólizas al azar
        num_polizas = random.randint(1, 3)
        polizas_cliente = random.sample(polizas_disponibles, num_polizas)
        
        resultado = "Sus pólizas de seguro:\n\n"
        
        for i, poliza in enumerate(polizas_cliente, 1):
            resultado += f"🛡️ PÓLIZA {i}\n"
            resultado += f"• Tipo: {poliza['tipo']}\n"
            resultado += f"• Número: {poliza['numero']}\n"
            resultado += f"• Cobertura: ${poliza['cobertura']:,.2f} USD\n"
            resultado += f"• Prima mensual: ${poliza['prima_mensual']:.2f} USD\n"
            resultado += f"• Estado: {poliza['estado']}\n"
            resultado += f"• Vencimiento: {poliza['vencimiento']}\n\n"
        
        resultado += "💡 Para renovar o modificar sus pólizas, visite cualquier sucursal o contacte a su asesor."
        
        return resultado
    
    def _arun(self, query: str):
        raise NotImplementedError("Este tool no soporta ejecución asíncrona")

def get_banking_tools():
    """Retorna la lista de herramientas bancarias disponibles"""
    return [
        SaldoCuentaTool(),
        InfoTarjetaCreditoTool(),
        CreditoBancarioTool(),
        PolizasTool()
    ]
