"""Small, stdlib-only order integration fixture for evidence-based audits."""

import json
import sqlite3
from typing import Protocol


class Broker(Protocol):
    def publish(self, topic: str, payload: str) -> None: ...


def create_sales_schema(connection: sqlite3.Connection) -> None:
    connection.execute(
        "CREATE TABLE orders (orders_pk INTEGER PRIMARY KEY, "
        "ship_to_line TEXT NOT NULL, orders_status_code TEXT NOT NULL, "
        "row_version INTEGER NOT NULL)"
    )
    connection.commit()


def create_fulfillment_schema(connection: sqlite3.Connection) -> None:
    connection.execute(
        "CREATE TABLE fulfillment_requests (order_id INTEGER NOT NULL, "
        "ship_to_line TEXT NOT NULL)"
    )
    connection.commit()


def _contract_message(event_type: str, row: tuple[int, str, str, int]) -> str:
    return json.dumps(
        {
            "type": event_type,
            "orders_pk": row[0],
            "ship_to_line": row[1],
            "orders_status_code": row[2],
            "row_version": row[3],
        }
    )


def accept_order(
    sales_db: sqlite3.Connection, broker: Broker, order_id: int, destination: str
) -> None:
    sales_db.execute(
        "INSERT INTO orders VALUES (?, ?, ?, ?)",
        (order_id, destination, "A", 1),
    )
    sales_db.commit()
    row = sales_db.execute(
        "SELECT orders_pk, ship_to_line, orders_status_code, row_version "
        "FROM orders WHERE orders_pk = ?",
        (order_id,),
    ).fetchone()
    broker.publish("sales.orders", _contract_message("OrderAccepted", row))


def revise_destination(
    sales_db: sqlite3.Connection, broker: Broker, order_id: int, destination: str
) -> None:
    sales_db.execute(
        "UPDATE orders SET ship_to_line = ?, row_version = row_version + 1 "
        "WHERE orders_pk = ?",
        (destination, order_id),
    )
    sales_db.commit()
    row = sales_db.execute(
        "SELECT orders_pk, ship_to_line, orders_status_code, row_version "
        "FROM orders WHERE orders_pk = ?",
        (order_id,),
    ).fetchone()
    broker.publish("sales.orders", _contract_message("OrderDestinationRevised", row))


def handle_order_message(fulfillment_db: sqlite3.Connection, payload: str) -> None:
    message = json.loads(payload)
    if message["type"] not in {"OrderAccepted", "OrderDestinationRevised"}:
        return
    fulfillment_db.execute(
        "INSERT INTO fulfillment_requests (order_id, ship_to_line) VALUES (?, ?)",
        (message["orders_pk"], message["ship_to_line"]),
    )
    fulfillment_db.commit()
