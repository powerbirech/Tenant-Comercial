from utils import run_fab_command

def take_ownership(workspace_name, dataset_id):
    print("✔️ Tomando controle do dataset")
    run_fab_command(f"takeownership /{workspace_name}.workspace/{dataset_id}.SemanticModel")

def bind_to_gateway(workspace_name, dataset_id, gateway_name):
    print(f"🔌 Associando ao gateway: {gateway_name}")
    run_fab_command(f"bindgateway /{workspace_name}.workspace/{dataset_id}.SemanticModel -g {gateway_name}")

def schedule_refresh(workspace_name, dataset_id, dias, horarios):
    print(f"📅 Configurando agendamento para dias: {dias} e horários: {horarios}")

    dias_mapeados = {
        "Sunday": "0",
        "Monday": "1",
        "Tuesday": "2",
        "Wednesday": "3",
        "Thursday": "4",
        "Friday": "5",
        "Saturday": "6"
    }

    dias_numericos = [dias_mapeados.get(dia, dia) for dia in dias]

    horarios_config = [f"{{\"frequency\":\"Daily\",\"time\":\"{hora}\",\"days\":[{','.join(dias_numericos)}]}}" for hora in horarios]

    # Monta string de configuração
    refresh_config = f"[{{\"enabled\":true,\"times\":[{','.join(horarios_config)}]}}]"

    run_fab_command(
        f"refresh schedule set -f /{workspace_name}.workspace/{dataset_id}.SemanticModel -c '{refresh_config}'"
    )

def create_public_link(workspace_name, report_name):
    print(f"🌐 Gerando link público para o relatório: {report_name}")
    link = run_fab_command(
        f"report createpubliclink -f /{workspace_name}.workspace/{report_name}.Report",
        capture_output=True
    )
    print(f"🔗 Link público gerado: {link}")
