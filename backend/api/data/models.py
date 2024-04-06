from typing import Any, Optional
from sqlalchemy import Dialect, ForeignKey, Time, Text, TypeDecorator
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.functions import current_timestamp
from pydantic import EmailStr

from backend.api.data.database import Base


class EmailType(TypeDecorator):
    """
    Custom Type for mashalling the pydantic EmailStr type to/from the database.
    """

    impl = Text

    def process_bind_param(self, value: Any | None, dialect: Dialect) -> Any:
        if value is not None:
            return str(value)

    def process_result_value(self, value: Any | None, dialect: Dialect) -> Any | None:
        if value is not None:
            return EmailStr(value)


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[Text]
    last_name: Mapped[Text]
    email: Mapped[EmailType] = mapped_column(unique=True)
    password: Mapped[Text]
    verified: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[Time] = mapped_column(default=current_timestamp())
    updated_at: Mapped[Time] = mapped_column(default=current_timestamp())

    def __repr__(self) -> str:
        return f"<Account id={self.id} email={self.email}>"


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Text]
    key: Mapped[Text] = mapped_column(unique=True)
    description: Mapped[Optional[Text]]
    author_id: Mapped[int] = mapped_column(
        ForeignKey("accounts.id", ondelete="CASCADE")
    )
    created_at: Mapped[Time] = mapped_column(default=current_timestamp())
    updated_at: Mapped[Time] = mapped_column(default=current_timestamp())

    def __repr__(self) -> str:
        return f"<Project id={self.id} key={self.key}>"


class Issue(Base):
    __tablename__ = "issues"

    id: Mapped[int] = mapped_column(primary_key=True)
    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects.id", ondelete="CASCADE")
    )
    title: Mapped[str]
    description: Mapped[Optional[Text]]
    author_id: Mapped[int] = mapped_column(
        ForeignKey("accounts.id", ondelete="CASCADE")
    )
    assignee_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("accounts.id", ondelete="CASCADE")
    )
    status: Mapped[Text]
    created_at: Mapped[Time] = mapped_column(default=current_timestamp())
    updated_at: Mapped[Time] = mapped_column(default=current_timestamp())

    def __repr__(self) -> str:
        return f"<Issue id={self.id} title={self.title}>"


class IssueRelationship(Base):
    __tablename__ = "issue_relationships"

    id: Mapped[int] = mapped_column(primary_key=True)
    parent_issue_id: Mapped[int] = mapped_column(
        ForeignKey("issues.id", ondelete="CASCADE")
    )
    child_issue_id: Mapped[int] = mapped_column(
        ForeignKey("issues.id", ondelete="CASCADE")
    )
    created_at: Mapped[Time] = mapped_column(default=current_timestamp())
    updated_at: Mapped[Time] = mapped_column(default=current_timestamp())

    def __repr__(self) -> str:
        return f"<IssueRelationship id={self.id}, parent_issue_id={self.parent_issue_id}, child_issue_id={self.child_issue_id}>"


class IssueBlocker(Base):
    __tablename__ = "issue_blockers"

    id: Mapped[int] = mapped_column(primary_key=True)
    blocked_issue_id: Mapped[int] = mapped_column(
        ForeignKey("issues.id", ondelete="CASCADE")
    )
    blocking_issue_id: Mapped[int] = mapped_column(
        ForeignKey("issues.id", ondelete="CASCADE")
    )
    created_at: Mapped[Time] = mapped_column(default=current_timestamp())
    updated_at: Mapped[Time] = mapped_column(default=current_timestamp())

    def __repr__(self) -> str:
        return f"<IssueBlocker id={self.id}, blocked_issue_id={self.blocked_issue_id}, blocking_issue_id={self.blocking_issue_id}>"
