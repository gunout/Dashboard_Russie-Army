# dashboard_defense_russie_avance.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Configuration de la page
st.set_page_config(
    page_title="Analyse Stratégique Avancée - Russie",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé avancé
st.markdown("""
<style>
    .main-header {
        font-size: 2.8rem;
        background: linear-gradient(45deg, #0033A0, #D52B1E, #FFFFFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .metric-card {
        background: linear-gradient(135deg, #0033A0, #0055B7);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 0.5rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .section-header {
        color: #D52B1E;
        border-bottom: 3px solid #0033A0;
        padding-bottom: 0.8rem;
        margin-top: 2rem;
        font-size: 1.8rem;
        font-weight: bold;
    }
    .nuclear-card {
        background: linear-gradient(135deg, #D52B1E, #FF6B35);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
    .navy-card {
        background: linear-gradient(135deg, #1e3c72, #2a5298);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .air-force-card {
        background: linear-gradient(135deg, #0055B7, #0077CC);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .army-card {
        background: linear-gradient(135deg, #8B0000, #B22222);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .strategic-card {
        background: linear-gradient(135deg, #4B0082, #8A2BE2);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .cyber-card {
        background: linear-gradient(135deg, #2d3436, #636e72);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

class DefenseRussieDashboardAvance:
    def __init__(self):
        self.branches_options = self.define_branches_options()
        self.programmes_options = self.define_programmes_options()
        self.nuclear_arsenal = self.define_nuclear_arsenal()
        self.missile_systems = self.define_missile_systems()
        
    def define_branches_options(self):
        return [
            "Forces Armées Russes", "Armée de Terre", "Marine Russe", 
            "Forces Aérospatiales", "Forces de Missiles Stratégiques",
            "Forces Aéroportées (VDV)", "Forces Spéciales", "Garde Nationale"
        ]
    
    def define_programmes_options(self):
        return [
            "Forces Nucléaires Stratégiques", "Modernisation des Armements",
            "Défense Anti-Missile", "Forces Aérospatiales",
            "Flotte Nord", "Systèmes Hypersoniques", "Guerre Électronique"
        ]
    
    def define_nuclear_arsenal(self):
        return {
            "RS-28 Sarmat": {"type": "ICBM", "portee": 18000, "ogives": 10, "statut": "Déploiement"},
            "RS-24 Yars": {"type": "ICBM", "portee": 12000, "ogives": 4, "statut": "Opérationnel"},
            "RS-26 Rubezh": {"type": "IRBM", "portee": 6000, "ogives": 3, "statut": "Test"},
            "Bulava": {"type": "SLBM", "portee": 10000, "ogives": 6, "statut": "Opérationnel"},
            "Kh-47M2 Kinzhal": {"type": "Missile Hypersonique", "portee": 2000, "ogives": 1, "statut": "Opérationnel"}
        }
    
    def define_missile_systems(self):
        return {
            "S-400 Triumf": {"type": "Défense AA", "portee": 400, "cibles": "Aéronefs, missiles", "statut": "Opérationnel"},
            "S-500 Prometheus": {"type": "Défense AA/ABM", "portee": 600, "cibles": "ICBM, satellites", "statut": "Déploiement"},
            "Iskander-M": {"type": "Missile Balistique", "portee": 500, "ogives": "Conventionnelle/Nucléaire", "statut": "Opérationnel"},
            "9K720 Kinzhal": {"type": "Hypersonique", "portee": 2000, "vitesse": "Mach 10", "statut": "Opérationnel"},
            "3M22 Zircon": {"type": "Missile Anti-Navire", "portee": 1000, "vitesse": "Mach 9", "statut": "Test"}
        }
    
    def generate_advanced_data(self, selection):
        """Génère des données avancées et détaillées pour la Russie"""
        annees = list(range(2000, 2028))
        
        config = self.get_advanced_config(selection)
        
        data = {
            'Annee': annees,
            'Budget_Defense_Mds': self.simulate_advanced_budget(annees, config),
            'Personnel_Milliers': self.simulate_advanced_personnel(annees, config),
            'PIB_Militaire_Pourcent': self.simulate_military_gdp_percentage(annees),
            'Exercices_Militaires': self.simulate_advanced_exercises(annees, config),
            'Readiness_Operative': self.simulate_advanced_readiness(annees),
            'Capacite_Dissuasion': self.simulate_advanced_deterrence(annees),
            'Temps_Mobilisation_Jours': self.simulate_advanced_mobilization(annees),
            'Tests_Missiles': self.simulate_missile_tests(annees),
            'Developpement_Technologique': self.simulate_tech_development(annees),
            'Capacite_Artillerie': self.simulate_artillery_capacity(annees),
            'Couverture_AD': self.simulate_air_defense_coverage(annees),
            'Resilience_Logistique': self.simulate_logistical_resilience(annees),
            'Cyber_Capabilities': self.simulate_cyber_capabilities(annees),
            'Production_Armements': self.simulate_weapon_production(annees)
        }
        
        # Données spécifiques aux programmes
        if 'nucleaire' in config.get('priorites', []):
            data.update({
                'Stock_Ogives_Nucleaires': self.simulate_nuclear_arsenal_size(annees),
                'Portee_Max_Missiles_Km': self.simulate_missile_range_evolution(annees),
                'Tetes_Multiples': self.simulate_mirv_development(annees),
                'Essais_Souterrains': self.simulate_underground_tests(annees)
            })
        
        if 'modernisation' in config.get('priorites', []):
            data.update({
                'Nouveaux_Systemes': self.simulate_new_systems(annees),
                'Taux_Modernisation': self.simulate_modernization_rate(annees),
                'Exportations_Armes': self.simulate_weapon_exports(annees)
            })
        
        if 'aerospatial' in config.get('priorites', []):
            data.update({
                'Satellites_Militaires': self.simulate_military_satellites(annees),
                'Capacite_Antisatellite': self.simulate_antisatellite_capability(annees),
                'Defense_Aerospatiale': self.simulate_aerospace_defense(annees)
            })
        
        if 'cyber' in config.get('priorites', []):
            data.update({
                'Attaques_Cyber_Reussies': self.simulate_cyber_attacks(annees),
                'Reseau_Commandement_Cyber': self.simulate_cyber_command(annees),
                'Cyber_Defense_Niveau': self.simulate_cyber_defense(annees)
            })
        
        return pd.DataFrame(data), config
    
    def get_advanced_config(self, selection):
        """Configuration avancée avec plus de détails pour la Russie"""
        configs = {
            "Forces Armées Russes": {
                "type": "armee_totale",
                "budget_base": 65.0,
                "personnel_base": 1000,
                "exercices_base": 150,
                "priorites": ["nucleaire", "modernisation", "aerospatial", "cyber", "conventionnel"],
                "doctrines": ["Dissuasion Stratégique", "Défense Active", "Opérations Hybrides"],
                "capacites_speciales": ["Forces Rapides", "Guerre Électronique", "Cyber Guerre"]
            },
            "Forces de Missiles Stratégiques": {
                "type": "branche_strategique",
                "personnel_base": 50,
                "exercices_base": 25,
                "priorites": ["icbm", "sibm", "mirv", "hypersonique"],
                "systemes_deployes": ["Sarmat", "Yars", "Bulava", "Kinzhal"],
                "zones_cibles": ["USA", "Europe", "Asie"]
            },
            "Marine Russe": {
                "type": "branche_navale",
                "personnel_base": 150,
                "exercices_base": 45,
                "priorites": ["sous-marins", "flotte_nord", "projection", "anti-acces"],
                "flottes_principales": ["Flotte Nord", "Flotte Pacifique", "Flotte Noire"],
                "navires_cles": ["Sous-marins Borei", "Croiseurs Kirov", "Frégates Gorshkov"]
            },
            "Forces Nucléaires Stratégiques": {
                "type": "programme_strategique",
                "budget_base": 12.0,
                "priorites": ["triade_nucleaire", "modernisation", "penetration"],
                "composantes": ["ICBM", "SLBM", "Bombardiers"],
                "estimations_stock": "6000 ogives nucléaires"
            }
        }
        
        return configs.get(selection, {
            "type": "branche",
            "personnel_base": 100,
            "exercices_base": 30,
            "priorites": ["defense_generique"]
        })
    
    def simulate_advanced_budget(self, annees, config):
        """Simulation avancée du budget avec variations géopolitiques"""
        budget_base = config.get('budget_base', 60.0)
        budgets = []
        for annee in annees:
            base = budget_base * (1 + 0.04 * (annee - 2000))
            # Variations selon événements géopolitiques
            if 2008 <= annee <= 2012:  # Modernisation post-Géorgie
                base *= 1.15
            elif 2014 <= annee <= 2016:  # Post-Crimée
                base *= 1.1
            elif annee >= 2020:  # Modernisation avancée
                base *= 1.2
            elif annee >= 2022:  # Opérations spéciales
                base *= 1.3
            budgets.append(base)
        return budgets
    
    def simulate_advanced_personnel(self, annees, config):
        """Simulation avancée des effectifs"""
        personnel_base = config.get('personnel_base', 800)
        return [personnel_base * (1 + 0.01 * (annee - 2000)) for annee in annees]
    
    def simulate_military_gdp_percentage(self, annees):
        """Pourcentage du PIB consacré à la défense"""
        return [3.5 + 0.3 * (annee - 2000) for annee in annees]
    
    def simulate_advanced_exercises(self, annees, config):
        """Exercices militaires avec saisonnalité"""
        base = config.get('exercices_base', 100)
        return [base + 5 * (annee - 2000) + 10 * np.sin(2 * np.pi * (annee - 2000)/4) for annee in annees]
    
    def simulate_advanced_readiness(self, annees):
        """Préparation opérationnelle avancée"""
        readiness = []
        for annee in annees:
            base = 70 + 1.2 * (annee - 2000)
            if annee >= 2008:  # Réformes militaires
                base += 10
            if annee >= 2014:  # Modernisation
                base += 8
            if annee >= 2020:  # Expérience opérationnelle
                base += 5
            readiness.append(min(base, 95))
        return readiness
    
    def simulate_advanced_deterrence(self, annees):
        """Capacité de dissuasion avancée"""
        deterrence = []
        for annee in annees:
            base = 85  # Héritage soviétique
            if annee >= 2008:
                base += 2  # Modernisation
            if annee >= 2018:
                base += 5  # Systèmes hypersoniques
            deterrence.append(min(base, 98))
        return deterrence
    
    def simulate_advanced_mobilization(self, annees):
        """Temps de mobilisation avancé"""
        return [max(30 - 0.5 * (annee - 2000), 7) for annee in annees]
    
    def simulate_missile_tests(self, annees):
        """Tests de missiles"""
        tests = []
        for annee in annees:
            if annee < 2008:
                tests.append(5)
            elif annee < 2014:
                tests.append(8 + (annee - 2008))
            else:
                tests.append(15 + 2 * (annee - 2014))
        return tests
    
    def simulate_tech_development(self, annees):
        """Développement technologique global"""
        return [min(75 + 1.5 * (annee - 2000), 95) for annee in annees]
    
    def simulate_artillery_capacity(self, annees):
        """Capacité d'artillerie"""
        return [min(80 + 1.2 * (annee - 2000), 95) for annee in annees]
    
    def simulate_air_defense_coverage(self, annees):
        """Couverture de défense anti-aérienne"""
        return [min(70 + 2 * (annee - 2000), 95) for annee in annees]
    
    def simulate_logistical_resilience(self, annees):
        """Résilience logistique"""
        return [min(65 + 2.5 * (annee - 2000), 92) for annee in annees]
    
    def simulate_cyber_capabilities(self, annees):
        """Capacités cybernétiques"""
        return [min(70 + 3 * (annee - 2000), 94) for annee in annees]
    
    def simulate_weapon_production(self, annees):
        """Production d'armements (indice)"""
        return [min(75 + 2 * (annee - 2000), 96) for annee in annees]
    
    def simulate_nuclear_arsenal_size(self, annees):
        """Évolution du stock d'ogives nucléaires"""
        stock = []
        for annee in annees:
            if annee < 2010:
                stock.append(8000 - 200 * (annee - 2000))  # Réduction START
            else:
                stock.append(6000 + 50 * (annee - 2010))  # Modernisation
        return [max(s, 4000) for s in stock]
    
    def simulate_missile_range_evolution(self, annees):
        """Évolution de la portée maximale des missiles"""
        portee = []
        for annee in annees:
            if annee < 2009:
                portee.append(11000)
            elif annee < 2017:
                portee.append(12000 + 500 * (annee - 2009))
            else:
                portee.append(18000)  # Sarmat opérationnel
        return portee
    
    def simulate_mirv_development(self, annees):
        """Développement des têtes multiples"""
        return [min(6 + 0.5 * (annee - 2000), 12) for annee in annees]
    
    def simulate_underground_tests(self, annees):
        """Essais souterrains et préparation"""
        return [min(85 + 1 * (annee - 2000), 98) for annee in annees]
    
    def simulate_new_systems(self, annees):
        """Nouveaux systèmes déployés"""
        return [min(5 + 2 * (annee - 2000), 50) for annee in annees]
    
    def simulate_modernization_rate(self, annees):
        """Taux de modernisation des équipements"""
        return [min(30 + 4 * (annee - 2000), 85) for annee in annees]
    
    def simulate_weapon_exports(self, annees):
        """Exportations d'armes (milliards USD)"""
        return [min(4 + 0.5 * (annee - 2000), 15) for annee in annees]
    
    def simulate_military_satellites(self, annees):
        """Satellites militaires en orbite"""
        return [min(80 + 5 * (annee - 2000), 150) for annee in annees]
    
    def simulate_antisatellite_capability(self, annees):
        """Capacité antisatellite"""
        return [min(60 + 3 * (annee - 2000), 95) for annee in annees]
    
    def simulate_aerospace_defense(self, annees):
        """Défense aérospatiale"""
        return [min(70 + 2.5 * (annee - 2000), 92) for annee in annees]
    
    def simulate_cyber_attacks(self, annees):
        """Attaques cyber réussies (estimation)"""
        return [min(20 + 3 * (annee - 2000), 100) for annee in annees]
    
    def simulate_cyber_command(self, annees):
        """Réseau de commandement cyber"""
        return [min(75 + 2 * (annee - 2000), 95) for annee in annees]
    
    def simulate_cyber_defense(self, annees):
        """Capacités de cyber défense"""
        return [min(70 + 2.5 * (annee - 2000), 92) for annee in annees]
    
    def display_advanced_header(self):
        """En-tête avancé avec plus d'informations"""
        st.markdown('<h1 class="main-header">⚡ ANALYSE STRATÉGIQUE AVANCÉE - FÉDÉRATION DE RUSSIE</h1>', 
                   unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("""
            <div style='text-align: center; background: linear-gradient(135deg, #0033A0, #D52B1E); 
            padding: 1rem; border-radius: 10px; color: white; margin: 1rem 0;'>
            <h3>🛡️ SYSTÈME DE DÉFENSE INTÉGRÉ DE LA FÉDÉRATION DE RUSSIE</h3>
            <p><strong>Analyse multidimensionnelle des capacités militaires et stratégiques (2000-2027)</strong></p>
            </div>
            """, unsafe_allow_html=True)
    
    def create_advanced_sidebar(self):
        """Sidebar avancé avec plus d'options"""
        st.sidebar.markdown("## 🎛️ PANEL DE CONTRÔLE AVANCÉ")
        
        # Sélection du type d'analyse
        type_analyse = st.sidebar.radio(
            "Mode d'analyse:",
            ["Analyse Branche Militaire", "Programmes Stratégiques", "Vue Systémique", "Scénarios Géopolitiques"]
        )
        
        if type_analyse == "Analyse Branche Militaire":
            selection = st.sidebar.selectbox("Branche militaire:", self.branches_options)
        elif type_analyse == "Programmes Stratégiques":
            selection = st.sidebar.selectbox("Programme stratégique:", self.programmes_options)
        elif type_analyse == "Vue Systémique":
            selection = "Forces Armées Russes"
        else:
            selection = "Scénarios Géopolitiques"
        
        # Options avancées
        st.sidebar.markdown("### 🔧 OPTIONS AVANCÉES")
        show_geopolitical = st.sidebar.checkbox("Contexte géopolitique", value=True)
        show_doctrinal = st.sidebar.checkbox("Analyse doctrinale", value=True)
        show_technical = st.sidebar.checkbox("Détails techniques", value=True)
        threat_assessment = st.sidebar.checkbox("Évaluation des menaces", value=True)
        
        # Paramètres de simulation
        st.sidebar.markdown("### ⚙️ PARAMÈTRES DE SIMULATION")
        scenario = st.sidebar.selectbox("Scénario:", ["Statut Quo", "Escalation OTAN", "Modernisation Accélérée", "Conflit Majeur"])
        
        return {
            'selection': selection,
            'type_analyse': type_analyse,
            'show_geopolitical': show_geopolitical,
            'show_doctrinal': show_doctrinal,
            'show_technical': show_technical,
            'threat_assessment': threat_assessment,
            'scenario': scenario
        }
    
    def display_strategic_metrics(self, df, config):
        """Métriques stratégiques avancées"""
        st.markdown('<h3 class="section-header">🎯 TABLEAU DE BORD STRATÉGIQUE</h3>', 
                   unsafe_allow_html=True)
        
        derniere_annee = df['Annee'].max()
        data_actuelle = df[df['Annee'] == derniere_annee].iloc[0]
        data_2000 = df[df['Annee'] == 2000].iloc[0]
        
        # Première ligne de métriques
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("""
            <div class="metric-card">
                <h4>💰 BUDGET DÉFENSE 2027</h4>
                <h2>{:.1f} Md$</h2>
                <p>📈 {:.1f}% du PIB</p>
            </div>
            """.format(data_actuelle['Budget_Defense_Mds'], data_actuelle['PIB_Militaire_Pourcent']), 
            unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="metric-card">
                <h4>👥 EFFECTIFS TOTAUX</h4>
                <h2>{:,.0f}K</h2>
                <p>⚔️ +{:.1f}% depuis 2000</p>
            </div>
            """.format(data_actuelle['Personnel_Milliers'], 
                     ((data_actuelle['Personnel_Milliers'] - data_2000['Personnel_Milliers']) / data_2000['Personnel_Milliers']) * 100), 
            unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="nuclear-card">
                <h4>☢️ TRIADE NUCLÉAIRE</h4>
                <h2>{:.0f}%</h2>
                <p>🚀 {} ogives stratégiques</p>
            </div>
            """.format(data_actuelle['Capacite_Dissuasion'], 
                     int(data_actuelle.get('Stock_Ogives_Nucleaires', 0))), 
            unsafe_allow_html=True)
        
        with col4:
            st.markdown("""
            <div class="strategic-card">
                <h4>🎯 SYSTÈMES HYPERSONIQUES</h4>
                <h2>{:.0f}%</h2>
                <p>⚡ {} systèmes déployés</p>
            </div>
            """.format(data_actuelle['Developpement_Technologique'], 
                     int(data_actuelle.get('Nouveaux_Systemes', 0))), 
            unsafe_allow_html=True)
        
        # Deuxième ligne de métriques
        col5, col6, col7, col8 = st.columns(4)
        
        with col5:
            reduction_temps = ((data_2000['Temps_Mobilisation_Jours'] - data_actuelle['Temps_Mobilisation_Jours']) / 
                             data_2000['Temps_Mobilisation_Jours']) * 100
            st.metric(
                "⏱️ Temps Mobilisation",
                f"{data_actuelle['Temps_Mobilisation_Jours']:.1f} jours",
                f"{reduction_temps:+.1f}%"
            )
        
        with col6:
            croissance_ad = ((data_actuelle['Couverture_AD'] - data_2000['Couverture_AD']) / 
                           data_2000['Couverture_AD']) * 100
            st.metric(
                "🛡️ Défense Anti-Aérienne",
                f"{data_actuelle['Couverture_AD']:.1f}%",
                f"{croissance_ad:+.1f}%"
            )
        
        with col7:
            if 'Portee_Max_Missiles_Km' in df.columns:
                croissance_portee = ((data_actuelle['Portee_Max_Missiles_Km'] - data_2000.get('Portee_Max_Missiles_Km', 11000)) / 
                                   data_2000.get('Portee_Max_Missiles_Km', 11000)) * 100
                st.metric(
                    "🎯 Portée Missiles Max",
                    f"{data_actuelle['Portee_Max_Missiles_Km']:,.0f} km",
                    f"{croissance_portee:+.1f}%"
                )
        
        with col8:
            st.metric(
                "📊 Préparation Opérationnelle",
                f"{data_actuelle['Readiness_Operative']:.1f}%",
                f"+{(data_actuelle['Readiness_Operative'] - data_2000['Readiness_Operative']):.1f}%"
            )
    
    def create_comprehensive_analysis(self, df, config):
        """Analyse complète multidimensionnelle"""
        st.markdown('<h3 class="section-header">📊 ANALYSE MULTIDIMENSIONNELLE</h3>', 
                   unsafe_allow_html=True)
        
        # Graphiques principaux
        col1, col2 = st.columns(2)
        
        with col1:
            # Évolution des capacités principales
            fig = go.Figure()
            
            capacites = ['Readiness_Operative', 'Capacite_Dissuasion', 'Cyber_Capabilities', 'Couverture_AD']
            noms = ['Préparation Opér.', 'Dissuasion Strat.', 'Capacités Cyber', 'Défense Anti-Aérienne']
            couleurs = ['#0033A0', '#D52B1E', '#2d3436', '#4B0082']
            
            for i, (cap, nom, couleur) in enumerate(zip(capacites, noms, couleurs)):
                if cap in df.columns:
                    fig.add_trace(go.Scatter(
                        x=df['Annee'], y=df[cap],
                        mode='lines', name=nom,
                        line=dict(color=couleur, width=4),
                        hovertemplate=f"{nom}: %{{y:.1f}}%<extra></extra>"
                    ))
            
            fig.update_layout(
                title="📈 ÉVOLUTION DES CAPACITÉS STRATÉGIQUES (2000-2027)",
                xaxis_title="Année",
                yaxis_title="Niveau de Capacité (%)",
                height=500,
                template="plotly_white",
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Analyse des programmes stratégiques
            strategic_data = []
            strategic_names = []
            
            if 'Stock_Ogives_Nucleaires' in df.columns:
                strategic_data.append(df['Stock_Ogives_Nucleaires'] / 100)  # Normalisation
                strategic_names.append('Stock Ogives (x100)')
            
            if 'Tests_Missiles' in df.columns:
                strategic_data.append(df['Tests_Missiles'])
                strategic_names.append('Tests de Missiles')
            
            if 'Nouveaux_Systemes' in df.columns:
                strategic_data.append(df['Nouveaux_Systemes'])
                strategic_names.append('Nouveaux Systèmes')
            
            if strategic_data:
                fig = make_subplots(specs=[[{"secondary_y": True}]])
                
                for i, (data, nom) in enumerate(zip(strategic_data, strategic_names)):
                    fig.add_trace(
                        go.Scatter(x=df['Annee'], y=data, name=nom,
                                 line=dict(width=4)),
                        secondary_y=(i > 0)
                    )
                
                fig.update_layout(
                    title="🚀 PROGRAMMES STRATÉGIQUES - ÉVOLUTION COMPARÉE",
                    height=500,
                    template="plotly_white"
                )
                st.plotly_chart(fig, use_container_width=True)
    
    def create_geopolitical_analysis(self, df, config):
        """Analyse géopolitique avancée"""
        st.markdown('<h3 class="section-header">🌍 CONTEXTE GÉOPOLITIQUE</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Cartes des zones d'influence
            st.markdown("""
            <div class="nuclear-card">
                <h4>🎯 ZONES D'INFLUENCE STRATÉGIQUE</h4>
                <p><strong>Europe Orientale:</strong> Biélorussie, Ukraine, Moldavie</p>
                <p><strong>Caucase:</strong> Arménie, Azerbaïdjan, Géorgie</p>
                <p><strong>Asie Centrale:</strong> Kazakhstan, Kirghizistan, Tadjikistan</p>
                <p><strong>Moyen-Orient:</strong> Syrie, Iran, Turquie</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Analyse des relations internationales
            st.markdown("""
            <div class="strategic-card">
                <h4>🌐 RELATIONS INTERNATIONALES</h4>
                <p><strong>OTAN:</strong> Opposition stratégique</p>
                <p><strong>Chine:</strong> Partenariat stratégique</p>
                <p><strong>Inde:</strong> Partenaire militaire traditionnel</p>
                <p><strong>OCS/BRICS:</strong> Coopération multipolaire</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Analyse des sanctions
            sanctions_data = {
                'Année': [2014, 2016, 2018, 2020, 2022, 2023],
                'Sanctions': ['Crimée', 'Syrie', 'Skripal', 'Nord Stream 2', 'Opération Spéciale', 'Nouvelles sanctions'],
                'Impact': [4, 5, 6, 5, 8, 9]  # sur 10
            }
            sanctions_df = pd.DataFrame(sanctions_data)
            
            fig = px.bar(sanctions_df, x='Année', y='Impact', 
                        title="📉 IMPACT DES SANCTIONS INTERNATIONALES",
                        labels={'Impact': 'Niveau d\'Impact'},
                        color='Impact',
                        color_continuous_scale='reds')
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
            
            # Indice d'autosuffisance
            autosuffisance = [min(70 + 2 * (annee - 2000), 95) for annee in df['Annee']]
            fig = px.area(x=df['Annee'], y=autosuffisance,
                         title="🛠️ AUTOSUFFISANCE MILITAIRE - IMPORT SUBSTITUTION",
                         labels={'x': 'Année', 'y': 'Niveau d\'Autosuffisance (%)'})
            fig.update_traces(fillcolor='rgba(213, 43, 30, 0.3)', line_color='#D52B1E')
            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)
    
    def create_technical_analysis(self, df, config):
        """Analyse technique détaillée"""
        st.markdown('<h3 class="section-header">🔬 ANALYSE TECHNIQUE AVANCÉE</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Analyse des systèmes d'armes
            systems_data = {
                'Système': ['T-14 Armata', 'Su-57 Felon', 'S-500 Prometheus', 
                           'RS-28 Sarmat', 'Sous-marin Borei', 'Avion MiG-41'],
                'Portée (km)': [5, 3500, 600, 18000, 10000, 4000],
                'Année Service': [2020, 2020, 2021, 2022, 2013, 2025],
                'Statut': ['Production', 'Opérationnel', 'Déploiement', 'Déploiement', 'Opérationnel', 'Développement']
            }
            systems_df = pd.DataFrame(systems_data)
            
            fig = px.scatter(systems_df, x='Portée (km)', y='Année Service', 
                           size='Portée (km)', color='Statut',
                           hover_name='Système', log_x=True,
                           title="🎯 CARACTÉRISTIQUES DES SYSTÈMES D'ARMES",
                           size_max=30)
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Analyse de la modernisation
            modernization_data = {
                'Domaine': ['Forces Terrestres', 'Forces Stratégiques', 
                          'Défense Aérienne', 'Marine', 'Forces Aérospatiales'],
                'Niveau 2000': [40, 70, 60, 50, 45],
                'Niveau 2027': [85, 95, 92, 80, 88]
            }
            modern_df = pd.DataFrame(modernization_data)
            
            fig = go.Figure()
            fig.add_trace(go.Bar(name='2000', x=modern_df['Domaine'], y=modern_df['Niveau 2000'],
                                marker_color='#0033A0'))
            fig.add_trace(go.Bar(name='2027', x=modern_df['Domaine'], y=modern_df['Niveau 2027'],
                                marker_color='#D52B1E'))
            
            fig.update_layout(title="📈 MODERNISATION DES CAPACITÉS MILITAIRES",
                             barmode='group', height=500)
            st.plotly_chart(fig, use_container_width=True)
            
            # Cartographie des installations
            st.markdown("""
            <div class="strategic-card">
                <h4>🗺️ INSTALLATIONS STRATÉGIQUES CLÉS</h4>
                <p><strong>Kozelsk:</strong> Base ICBM</p>
                <p><strong>Severomorsk:</strong> QG Flotte Nord</p>
                <p><strong>Plesetsk:</strong> Cosmodrome militaire</p>
                <p><strong>Kronstadt:</strong> Base sous-marine</p>
            </div>
            """, unsafe_allow_html=True)
    
    def create_doctrinal_analysis(self, config):
        """Analyse doctrinale avancée"""
        st.markdown('<h3 class="section-header">📚 ANALYSE DOCTRINALE</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="nuclear-card">
                <h4>🎯 DOCTRINE DE DÉFENSE</h4>
                <p><strong>Dissuasion stratégique:</strong> Primauté nucléaire</p>
                <p><strong>Défense active:</strong> Profondeur stratégique</p>
                <p><strong>Flexibilité:</strong> Adaptation aux menaces</p>
                <p><strong>Riposte proportionnée:</strong> Échelle de réponse</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="strategic-card">
                <h4>⚡ DOCTRINE DES OPÉRATIONS HYBRIDES</h4>
                <p><strong>Guerre non-linéaire:</strong> Actions indirectes</p>
                <p><strong>Guerre informationnelle:</strong> Domination cognitive</p>
                <p><strong>Cyber guerre:</strong> Actions numériques</p>
                <p><strong>Forces spéciales:</strong> Opérations déniables</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="air-force-card">
                <h4>🛡️ STRATÉGIE DE DÉFENSE INTÉGRÉE</h4>
                <p><strong>Défense aérospatiale:</strong> Couverture unifiée</p>
                <p><strong>Coordination interarmées:</strong> Synergie des forces</p>
                <p><strong>Réseaux C4ISR:</strong> Commandement intégré</p>
                <p><strong>Mobilité stratégique:</strong> Projection de puissance</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Principes opérationnels
        st.markdown("""
        <div class="navy-card">
            <h4>🎖️ PRINCIPES OPÉRATIONNELS DES FORCES ARMÉES RUSSES</h4>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-top: 1rem;">
                <div><strong>• Concentration des efforts:</strong> Masser les forces décisives</div>
                <div><strong>• Surprise et tromperie:</strong> Maskirovka opérationnelle</div>
                <div><strong>• Manœuvre opérationnelle:</strong> Mobilité et flexibilité</div>
                <div><strong>• Économie des forces:</strong> Utilisation rationnelle</div>
                <div><strong>• Coordination des armes:</strong> Combat interarmes</div>
                <div><strong>• Soutien logistique:</strong> Approvisionnement continu</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    def create_threat_assessment(self, df, config):
        """Évaluation avancée des menaces"""
        st.markdown('<h3 class="section-header">⚠️ ÉVALUATION STRATÉGIQUE DES MENACES</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Matrice des menaces
            threats_data = {
                'Type de Menace': ['Expansion OTAN', 'Frappe de Décapitation', 'Guerre Cyber', 
                                 'Encerclement Stratégique', 'Instabilité Périphérique', 'Sanctions Économiques'],
                'Probabilité': [0.8, 0.3, 0.9, 0.7, 0.6, 0.9],
                'Impact': [0.8, 0.9, 0.7, 0.8, 0.5, 0.7],
                'Niveau Préparation': [0.9, 0.95, 0.8, 0.7, 0.6, 0.5]
            }
            threats_df = pd.DataFrame(threats_data)
            
            fig = px.scatter(threats_df, x='Probabilité', y='Impact', 
                           size='Niveau Préparation', color='Type de Menace',
                           title="🎯 MATRICE RISQUES - PROBABILITÉ VS IMPACT",
                           size_max=30)
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Capacités de réponse
            response_data = {
                'Scénario': ['Conflit Régional', 'Crise Nucléaire', 'Guerre Cyber', 
                           'Opérations Hybrides', 'Intervention Étrangère'],
                'Dissuasion': [0.7, 1.0, 0.3, 0.8, 0.9],
                'Défense': [0.8, 0.4, 0.7, 0.6, 0.8],
                'Riposte': [0.9, 1.0, 0.8, 0.9, 0.95]
            }
            response_df = pd.DataFrame(response_data)
            
            fig = go.Figure(data=[
                go.Bar(name='Dissuasion', x=response_df['Scénario'], y=response_df['Dissuasion']),
                go.Bar(name='Défense', x=response_df['Scénario'], y=response_df['Défense']),
                go.Bar(name='Riposte', x=response_df['Scénario'], y=response_df['Riposte'])
            ])
            fig.update_layout(title="🛡️ CAPACITÉS DE RÉPONSE PAR SCÉNARIO",
                             barmode='group', height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        # Recommandations stratégiques
        st.markdown("""
        <div class="nuclear-card">
            <h4>🎯 RECOMMANDATIONS STRATÉGIQUES</h4>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-top: 1rem;">
                <div><strong>• Modernisation nucléaire:</strong> Triade avancée</div>
                <div><strong>• Défense aérospatiale:</strong> Bouclier intégré</div>
                <div><strong>• Capacités conventionnelles:</strong> Forces rapides</div>
                <div><strong>• Guerre électronique:</strong> Supériorité spectrale</div>
                <div><strong>• Cyber défense:</strong> Résilience numérique</div>
                <div><strong>• Coopération stratégique:</strong> Partenariats sélectifs</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    def create_nuclear_database(self):
        """Base de données des systèmes nucléaires"""
        st.markdown('<h3 class="section-header">☢️ BASE DE DONNÉES DES SYSTÈMES STRATÉGIQUES</h3>', 
                   unsafe_allow_html=True)
        
        nuclear_data = []
        for nom, specs in self.nuclear_arsenal.items():
            nuclear_data.append({
                'Système': nom,
                'Type': specs['type'],
                'Portée (km)': specs['portee'],
                'Ogives': specs['ogives'],
                'Statut': specs['statut'],
                'Classification': 'Offensif' if specs['type'] in ['ICBM', 'SLBM'] else 'Défensif'
            })
        
        nuclear_df = pd.DataFrame(nuclear_data)
        
        # Affichage interactif
        col1, col2 = st.columns([2, 1])
        
        with col1:
            fig = px.scatter(nuclear_df, x='Portée (km)', y='Ogives',
                           size='Portée (km)', color='Classification',
                           hover_name='Système', log_x=True,
                           title="☢️ CARACTÉRISTIQUES DES SYSTÈMES NUCLÉAIRES",
                           size_max=30)
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("""
            <div class="nuclear-card">
                <h4>📋 INVENTAIRE STRATÉGIQUE</h4>
            """, unsafe_allow_html=True)
            
            for systeme in nuclear_data:
                st.markdown(f"""
                <div style="background: rgba(255,255,255,0.1); padding: 0.5rem; margin: 0.2rem 0; border-radius: 5px;">
                    <strong>{systeme['Système']}</strong><br>
                    🎯 {systeme['Type']} • 🚀 {systeme['Portée (km)']:,} km<br>
                    💣 {systeme['Ogives']} ogives • {systeme['Statut']}
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
    
    def run_advanced_dashboard(self):
        """Exécute le dashboard avancé complet"""
        # Sidebar avancé
        controls = self.create_advanced_sidebar()
        
        # Header avancé
        self.display_advanced_header()
        
        # Génération des données avancées
        df, config = self.generate_advanced_data(controls['selection'])
        
        # Navigation par onglets avancés
        tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
            "📊 Tableau de Bord", 
            "🔬 Analyse Technique", 
            "🌍 Contexte Géopolitique", 
            "📚 Doctrine Militaire",
            "⚠️ Évaluation Menaces",
            "☢️ Systèmes Stratégiques",
            "💎 Synthèse Stratégique"
        ])
        
        with tab1:
            self.display_strategic_metrics(df, config)
            self.create_comprehensive_analysis(df, config)
        
        with tab2:
            self.create_technical_analysis(df, config)
        
        with tab3:
            if controls['show_geopolitical']:
                self.create_geopolitical_analysis(df, config)
        
        with tab4:
            if controls['show_doctrinal']:
                self.create_doctrinal_analysis(config)
        
        with tab5:
            if controls['threat_assessment']:
                self.create_threat_assessment(df, config)
        
        with tab6:
            if controls['show_technical']:
                self.create_nuclear_database()
        
        with tab7:
            self.create_strategic_synthesis(df, config, controls)
    
    def create_strategic_synthesis(self, df, config, controls):
        """Synthèse stratégique finale"""
        st.markdown('<h3 class="section-header">💎 SYNTHÈSE STRATÉGIQUE - FÉDÉRATION DE RUSSIE</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="nuclear-card">
                <h4>🏆 POINTS FORTS STRATÉGIQUES</h4>
                <div style="margin-top: 1rem;">
                    <div class="strategic-card" style="margin: 0.5rem 0;">
                        <strong>☢️ Supériorité Nucléaire</strong>
                        <p>Triade nucléaire moderne avec capacités de pénétration avancées</p>
                    </div>
                    <div class="navy-card" style="margin: 0.5rem 0;">
                        <strong>🚀 Technologies Avancées</strong>
                        <p>Systèmes hypersoniques et armes à énergie dirigée opérationnelles</p>
                    </div>
                    <div class="air-force-card" style="margin: 0.5rem 0;">
                        <strong>🛡️ Défense Intégrée</strong>
                        <p>Réseaux de défense aérospatiale les plus avancés au monde</p>
                    </div>
                    <div class="army-card" style="margin: 0.5rem 0;">
                        <strong>🌐 Expérience Opérationnelle</strong>
                        <p>Forces aguerries par des conflits récents et exercices à grande échelle</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="strategic-card">
                <h4>🎯 DÉFIS ET VULNÉRABILITÉS</h4>
                <div style="margin-top: 1rem;">
                    <div class="strategic-card" style="margin: 0.5rem 0;">
                        <strong>💸 Contraintes Économiques</strong>
                        <p>Sanctions internationales affectant la modernisation</p>
                    </div>
                    <div class="strategic-card" style="margin: 0.5rem 0;">
                        <strong>🔧 Dépendance aux Importations</strong>
                        <p>Certains composants high-tech encore importés</p>
                    </div>
                    <div class="strategic-card" style="margin: 0.5rem 0;">
                        <strong>🌐 Isolement Diplomatique</strong>
                        <p>Relations tendues avec l'Occident limitant la coopération</p>
                    </div>
                    <div class="strategic-card" style="margin: 0.5rem 0;">
                        <strong>⚡ Usure des Équipements</strong>
                        <p>Certains systèmes conventionnels nécessitent modernisation</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Perspectives futures
        st.markdown("""
        <div class="metric-card">
            <h4>🔮 PERSPECTIVES STRATÉGIQUES 2027-2035</h4>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-top: 1rem;">
                <div>
                    <h5>🚀 DOMAINE NUCLÉAIRE</h5>
                    <p>• ICBM Sarmat pleinement opérationnel<br>• SLBM Bulava-M<br>• Bombardier PAK-DA<br>• Ogives hypersoniques</p>
                </div>
                <div>
                    <h5>🛡️ DÉFENSE AÉROSPATIALE</h5>
                    <p>• S-500 déployé massivement<br>• Systèmes laser opérationnels<br>• Satellites militaires nouvelle génération<br>• Défense antisatellite</p>
                </div>
                <div>
                    <h5>💻 DOMAINE CYBER</h5>
                    <p>• Cyber commandement unifié<br>• IA militaire opérationnelle<br>• Guerre électronique avancée<br>• Protection infrastructures critiques</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Recommandations finales
        st.markdown("""
        <div class="nuclear-card">
            <h4>🎖️ RECOMMANDATIONS STRATÉGIQUES FINALES</h4>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-top: 1rem;">
                <div>
                    <h5>🛡️ DÉFENSE ACTIVE</h5>
                    <p>• Modernisation continue de la triade nucléaire<br>
                    • Déploiement massif des systèmes S-500<br>
                    • Développement des capacités hypersoniques<br>
                    • Renforcement de la cyber défense</p>
                </div>
                <div>
                    <h5>⚡ DISSUASION AVANCÉE</h5>
                    <p>• Maintien de la parité stratégique<br>
                    • Développement capacités antisatellites<br>
                    • Modernisation forces conventionnelles<br>
                    • Coopération avec partenaires stratégiques</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Lancement du dashboard avancé
if __name__ == "__main__":
    dashboard = DefenseRussieDashboardAvance()
    dashboard.run_advanced_dashboard()