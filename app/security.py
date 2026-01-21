from fastapi import Header, HTTPException, status


def require_role(required_role: str):
    def checker(x_role: str = Header(None)):
        if x_role is None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Missing role"
            )

        if x_role != required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden"
            )

        return None

    return checker
