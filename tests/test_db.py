from sqlalchemy import select

from fastapi_madr.models import Account


def test_create_account(session):
    new_account = Account(
        username='victor',
        email='victor@contreras.com',
        password='teste'
    )

    session.add(new_account)
    session.commit()
    session.refresh(new_account)

    account = session.scalar(
        select(Account).where(Account.username == 'victor')
    )

    assert account.username == 'victor'
