from ingestors import FundsExplorer


if __name__ == "__main__":
    ingestor = FundsExplorer(
        wallet=[
            "HGCR11",
            # "XPLG11",
            # "KNRI11",
            # "HGRU11",
            # "TORD11",
            # "VINO11",
            # "IRDM11",
            # "MXRF11",
            # "MGFF11",
        ]
    )
    ingestor.get_data()
    ingestor.save_data(filename="fundos.csv")
