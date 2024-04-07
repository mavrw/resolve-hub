from datetime import datetime
from typing import Any, List, Optional
from sqlalchemy import Dialect, ForeignKey, String, TypeDecorator
from sqlalchemy.orm import Mapped, mapped_column, declarative_base
from sqlalchemy.sql.functions import current_timestamp
from pydantic import EmailStr


# ==============================================================================
# Type Decorators
# ==============================================================================


class EmailType(TypeDecorator):
    """
    Custom Type for mashalling the pydantic EmailStr type to/from the database.
    """

    impl = String

    def process_bind_param(self, value: Any | None, dialect: Dialect) -> Any:
        if value is not None:
            return str(value)

    def process_result_value(self, value: Any | None, dialect: Dialect) -> Any | None:
        if value is not None:
            return EmailStr(value)


# ==============================================================================
# Models
# ==============================================================================


Base = declarative_base()


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str] = mapped_column(EmailType(), unique=True)
    password: Mapped[str]
    verified: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(default=current_timestamp())
    updated_at: Mapped[datetime] = mapped_column(default=current_timestamp())

    def __repr__(self) -> str:
        return f"<Account id={self.id} email={self.email}>"


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    key: Mapped[str] = mapped_column(unique=True)
    description: Mapped[Optional[str]]
    author_id: Mapped[int] = mapped_column(
        ForeignKey("accounts.id", ondelete="CASCADE")
    )
    created_at: Mapped[datetime] = mapped_column(default=current_timestamp())
    updated_at: Mapped[datetime] = mapped_column(default=current_timestamp())

    def __repr__(self) -> str:
        return f"<Project id={self.id} key={self.key}>"


class Issue(Base):
    __tablename__ = "issues"

    id: Mapped[int] = mapped_column(primary_key=True)
    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects.id", ondelete="CASCADE")
    )
    title: Mapped[str]
    description: Mapped[Optional[str]]
    author_id: Mapped[int] = mapped_column(
        ForeignKey("accounts.id", ondelete="CASCADE")
    )
    assignee_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("accounts.id", ondelete="CASCADE")
    )
    status: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(default=current_timestamp())
    updated_at: Mapped[datetime] = mapped_column(default=current_timestamp())

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
    created_at: Mapped[datetime] = mapped_column(default=current_timestamp())
    updated_at: Mapped[datetime] = mapped_column(default=current_timestamp())

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
    created_at: Mapped[datetime] = mapped_column(default=current_timestamp())
    updated_at: Mapped[datetime] = mapped_column(default=current_timestamp())

    def __repr__(self) -> str:
        return f"<IssueBlocker id={self.id}, blocked_issue_id={self.blocked_issue_id}, blocking_issue_id={self.blocking_issue_id}>"


class IssueLabel(Base):
    __tablename__ = "issue_labels"

    id: Mapped[int] = mapped_column(primary_key=True)
    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects.id", ondelete="CASCADE")
    )
    issue_id: Mapped[int] = mapped_column(ForeignKey("issues.id", ondelete="CASCADE"))
    text: Mapped[str]
    color: Mapped[str] = mapped_column(default="#424242")

    def __repr__(self) -> str:
        return f"<IssueLabel id={self.id} text={self.text} project_id={self.project_id} issue_id={self.issue_id}>"
