from transaction import Transaction

class TransactionRepository:
    def __init__(self, session: Session):
        """
        Initialises the TransactionRepository with a database session.

        Args:
            session (Session): SQLAlchemy database session.
        """
        self.session = session

    def get_by_id(self, transaction_id: int) -> Transaction | None:
        """
        Retrieves a transaction by its ID.

        Args:
            transaction_id (int): The ID of the transaction.

        Returns:
            Transaction | None: The Transaction object if found, otherwise None.
        """
        return self.session.query(Transaction).get(transaction_id)

    def get_all(self) -> list[Transaction]:
        """
        Retrieves all transactions.

        Returns:
            list[Transaction]: A list of all Transaction objects.
        """
        return self.session.query(Transaction).all()

    def get_by_instrument(self, instrument_id: int) -> list[Transaction]:
        """
        Retrieves all transactions for a given instrument.

        Args:
            instrument_id (int): The ID of the instrument.

        Returns:
            list[Transaction]: A list of Transaction objects related to the instrument.
        """
        return self.session.query(Transaction).filter_by(instrument_id=instrument_id).all()

    def save(self, transaction: Transaction) -> None:
        """
        Saves a transaction to the database.

        Args:
            transaction (Transaction): The Transaction object to save.
        """
        self.session.add(transaction)
        self.session.commit()

    def delete(self, transaction: Transaction) -> None:
        """
        Deletes a transaction from the database.

        Args:
            transaction (Transaction): The Transaction object to delete.
        """
        self.session.delete(transaction)
        self.session.commit()