import json
from pathlib import Path
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionFornecerSuporte(Action):
    def name(self) -> Text:
        return "action_fornecer_suporte"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        problema = tracker.get_slot("problema")

        base_path = Path(__file__).resolve().parent.parent / "base_suporte.json"

        try:
            with open(base_path, "r", encoding="utf-8") as f:
                base = json.load(f)
        except Exception:
            dispatcher.utter_message(
                text="Ocorreu um erro ao consultar a base de suporte. Vou encaminhar você para um atendente humano."
            )
            return []

        if not problema:
            dispatcher.utter_message(
                text="Não consegui identificar seu problema. Você pode informar se é acesso à conta, mudança de plano, app não funciona ou pagamento?"
            )
            return []

        info = base.get(problema)

        if not info:
            dispatcher.utter_message(
                text="Não encontrei esse problema na base de conhecimento. Vou encaminhar você para um atendente humano."
            )
            return [SlotSet("problema", "problema_complexo")]

        if info.get("encaminhar_humano", False):
            dispatcher.utter_message(
                text="Seu caso precisa de análise humana. Vou encaminhar você para um atendente."
            )
            return []

        passos = "\n".join([f"{i+1}. {passo}" for i, passo in enumerate(info["solucao"])])
        artigo = info.get("artigo", "Não disponível")

        mensagem = (
            f"Entendi. Seu problema é: {problema}\n\n"
            f"Siga estes passos:\n{passos}\n\n"
            f"Artigo de ajuda: {artigo}\n\n"
            f"Se isso não resolver, digite: 'quero falar com um atendente'."
        )

        dispatcher.utter_message(text=mensagem)
        return [SlotSet("problema", problema)]