import networkx as nx
import numpy as np

class ImpactSimulator:
    """
    Agente de simulación de impacto para probar narrativas en un entorno virtual.
    Utiliza un modelo de grafo para predecir la difusión de una idea.
    """
    def __init__(self):
        self.graph = self._create_social_graph()

    def _create_social_graph(self):
        """
        Crea un grafo social simulado para el testeo.
        Nodos: individuos o comunidades
        Aristas: conexiones o relaciones
        """
        G = nx.Graph()
        # Nodos principales: la comunidad objetivo y nodos clave
        nodes = ['nodo_objetivo', 'influencer_A', 'influencer_B', 'comunidad_X', 'comunidad_Y']
        G.add_nodes_from(nodes)
        
        # Conexiones: aristas para simular relaciones
        edges = [
            ('nodo_objetivo', 'influencer_A'),
            ('influencer_A', 'comunidad_X'),
            ('influencer_B', 'comunidad_Y'),
            ('comunidad_X', 'comunidad_Y'),
            ('influencer_A', 'influencer_B')
        ]
        G.add_edges_from(edges)
        
        return G

    def simulate_diffusion(self, idea, starting_node='nodo_objetivo', iterations=5):
        """
        Simula la difusión de una idea a través del grafo.
        
        :param idea: La narrativa a simular (ej. "quiero una banana").
        :param starting_node: El punto de entrada de la idea.
        :param iterations: El número de ciclos de difusión.
        :return: Un diccionario con el reporte de la simulación.
        """
        if starting_node not in self.graph:
            return {"estado": "fallido", "motivo": f"El nodo inicial '{starting_node}' no existe en el grafo."}

        # Estado inicial del sistema: solo el nodo de origen conoce la idea
        diffusion_state = {node: 0.0 for node in self.graph.nodes()}
        diffusion_state[starting_node] = 1.0  # El nodo de inicio está 100% "infectado" con la idea
        
        report = {
            "idea_simulada": idea,
            "punto_de_entrada": starting_node,
            "historial_de_difusion": []
        }

        # Simulación paso a paso (modelo de difusión simplificado)
        for i in range(iterations):
            new_state = diffusion_state.copy()
            for node in self.graph.nodes():
                if new_state[node] > 0:  # Si el nodo ya tiene la idea
                    for neighbor in self.graph.neighbors(node):
                        # La probabilidad de infección es proporcional a la fuerza de la conexión
                        infection_prob = 0.5 * new_state[node] * np.random.rand()
                        new_state[neighbor] = max(new_state[neighbor], infection_prob)
            
            diffusion_state = new_state
            
            # Registrar el estado de la red en cada iteración
            report['historial_de_difusion'].append({
                "iteracion": i + 1,
                "estado_de_la_red": {n: round(v, 2) for n, v in diffusion_state.items()}
            })

        # Evaluación final del impacto
        total_impact = sum(diffusion_state.values()) / len(self.graph.nodes())
        report['impacto_total_promedio'] = round(total_impact, 2)
        
        return report
