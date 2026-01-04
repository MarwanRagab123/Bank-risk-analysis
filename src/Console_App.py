from src.DataManager.data_manger import DataManagerc
from src.FeatureBuilder.feature_builder import FeatureBuilder
from src.RiskScore.risk_score import RiskScorer
from src.TransactionFlagger.transaction_flagger import TransactionFlagger
from src.GenerateReports.generate_reports import GenerateReports
from src.ConsoleSummary.console_summary import SummaryConsole
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from constant.shape import PROJECT_TITLE, PROJECT_NAME,display_welcome_banner


class ConsoleApp:
    def __init__(self):
        self.data = None
        self.dataManager = DataManagerc()
        self.featureBuild = FeatureBuilder()
        self.riskScore = RiskScorer()
        self.flagger = TransactionFlagger()
        self.generateReports = GenerateReports()
        self.summaryConsole = SummaryConsole()
        self.console = Console()

    def run(self):
        self.console.print(Panel("[bold white]Bank Analysis Project[/]", style="bold cyan"))
        display_welcome_banner(self)

        while True:
            menu = Table(show_header=False, box=None)
            menu.add_column("Option", style="bold cyan", width=6)
            menu.add_column("Description")
            menu.add_row("1", "Load dataset(s)")
            menu.add_row("2", "Clean and validate data")
            menu.add_row("3", "Build features")
            menu.add_row("4", "Score customers")
            menu.add_row("5", "Flag suspicious transactions")
            menu.add_row("6", "Export reports")
            menu.add_row("7", "Display summary in console")
            menu.add_row("0", "Exit application")
            self.console.print(menu)

            try:
                choice = Prompt.ask("Enter Your Choice").strip()

                if not choice:
                    self.console.print("[red]Error![/] Please enter a number from the menu!\n")
                    continue

                choice = int(choice)

                if choice == 1:
                    try:
                        self.console.print("[yellow]Loading dataset...[/]")
                        self.data = self.dataManager.load_data("data/test_data.csv")
                        self.console.print("[green]Data loaded successfully![/]\n")
                    except FileNotFoundError as e:
                        print(f"Error: {e}\n")
                    except Exception as e:
                        print(f"Error: {e}\n")

                elif choice == 2:
                    if self.data is not None:
                        try:
                            self.console.print("[yellow]Cleaning data...[/]")
                            self.data = self.dataManager.clean_data(self.data)
                            self.console.print("[green]Data cleaned successfully![/]\n")
                        except ValueError as e:
                            print(f"Error: {e}\n")
                        except Exception as e:
                            print(f"Error: {e}\n")
                    else:
                        print("Error: No data loaded! Please load data first.\n")

                elif choice == 3:
                    if self.data is not None:
                        try:
                            self.console.print("[yellow]Building features...[/]")
                            self.data = self.featureBuild.built_feature(self.data)
                            self.console.print("[green]Features built successfully![/]\n")

                        except ValueError as e:
                            print(f"Error: {e}\n")
                        except Exception as e:
                            print(f"Error: {e}\n")
                    else:
                        print("Error: No data loaded! Please load data first.\n")

                elif choice == 4:
                    if self.data is not None:
                        try:
                            self.console.print("[yellow]Computing risk scores for each customer...[/]")
                            self.data = self.riskScore.compute_scores(self.data)
                            self.console.print("[green]Risk scores computed successfully![/]\n")

                        except ValueError as e:
                            print(f"Error: {e}\n")
                        except Exception as e:
                            print(f"Error: {e}\n")
                    else:
                        print("Error: No data loaded! Please load data first.\n")

                elif choice == 5:
                    if self.data is not None:
                        try:
                            self.console.print("[yellow]Flagging suspicious transactions...[/]")
                            self.flagger.is_suspicious(self.data)
                            self.console.print("[green]Suspicious transactions flagged successfully![/]\n")
                        except ValueError as e:
                            print(f"Error: {e}\n")
                        except Exception as e:
                            print(f"Error: {e}\n")
                    else:
                        print("Error: No data loaded! Please load data first.\n")

                elif choice == 6:
                    if self.data is not None:
                        try:
                            self.console.print("[yellow]Generating reports...[/]")
                            self.generateReports.generate_reports(self.data)
                            self.console.print("[green]Reports generated successfully![/]\n")
                        except Exception as e:
                            print(f"Error: {e}\n")
                    else:
                        print("Error: No data loaded! Please load data first.\n")

                elif choice == 7:
                    if self.data is not None:
                        try:
                            self.summaryConsole.summary_console(self.data)
                        except Exception as e:
                            self.console.print(f"[red]Error:[/] {e}\n")
                    else:
                        print("Error: No data loaded! Please load data first.\n")

                elif choice == 0:
                    self.console.print("\n[bold]Thank you for using the application![/]")
                    break

                else:
                    self.console.print("[red]Error![/] Please choose a valid number from the menu!\n")



            except ValueError:
                self.console.print("[red]Error![/] Please enter a valid number!\n")