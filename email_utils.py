"""
email_utils.py - Email Placeholder Handler for RA-ProAgent

This module handles email placeholder replacement in apa_case_storage.
When loading case data, it automatically replaces {{USER_EMAIL}} and {{USER_EMAIL_CC}}
with the actual email addresses set in environment variables.

Usage:
------
1. Set environment variables:
   export USER_EMAIL="your_email@example.com"
   export USER_EMAIL_CC="your_cc_email@example.com"  # Optional

2. Use in code:
   from email_utils import replace_email_placeholders, get_user_emails
   
   # Get user emails
   primary, cc = get_user_emails()
   
   # Replace placeholders in a string
   content = replace_email_placeholders(content)
   
   # Replace placeholders in all strings within a dict
   data = replace_email_placeholders_in_dict(data)
"""

import os
import json
import re
from typing import Tuple, Optional, Any, Dict, List, Union


# Placeholder definitions
EMAIL_PLACEHOLDER = "{{USER_EMAIL}}"
EMAIL_CC_PLACEHOLDER = "{{USER_EMAIL_CC}}"

# Environment variable names
ENV_USER_EMAIL = "USER_EMAIL"
ENV_USER_EMAIL_CC = "USER_EMAIL_CC"


def get_user_emails() -> Tuple[str, str]:
    """
    Get user email addresses from environment variables.
    
    Returns:
        Tuple[str, str]: (primary_email, cc_email)
        
    Raises:
        ValueError: If USER_EMAIL environment variable is not set
    """
    primary_email = os.environ.get(ENV_USER_EMAIL)
    cc_email = os.environ.get(ENV_USER_EMAIL_CC)
    
    if not primary_email:
        raise ValueError(
            f"Environment variable {ENV_USER_EMAIL} is not set!\n"
            f"Please run: export {ENV_USER_EMAIL}=\"your_email@example.com\""
        )
    
    # If CC email is not set, use primary email
    if not cc_email:
        cc_email = primary_email
        
    return primary_email, cc_email


def validate_email(email: str) -> bool:
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def replace_email_placeholders(content: str) -> str:
    """
    Replace email placeholders in a string.
    
    Args:
        content: String containing placeholders
        
    Returns:
        String with placeholders replaced
    """
    if not content or not isinstance(content, str):
        return content
        
    primary_email, cc_email = get_user_emails()
    
    content = content.replace(EMAIL_PLACEHOLDER, primary_email)
    content = content.replace(EMAIL_CC_PLACEHOLDER, cc_email)
    
    return content


def replace_email_placeholders_in_dict(data: Any) -> Any:
    """
    Recursively replace email placeholders in all strings within a dict/list.
    
    Args:
        data: Dict, list, or other data
        
    Returns:
        Data with placeholders replaced (preserving original structure)
    """
    if isinstance(data, str):
        return replace_email_placeholders(data)
    elif isinstance(data, dict):
        return {k: replace_email_placeholders_in_dict(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [replace_email_placeholders_in_dict(item) for item in data]
    else:
        return data


def load_json_with_email_replacement(filepath: str) -> Dict:
    """
    Load a JSON file and replace email placeholders.
    
    Args:
        filepath: Path to JSON file
        
    Returns:
        Dict with placeholders replaced
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    return replace_email_placeholders_in_dict(data)


def load_file_with_email_replacement(filepath: str) -> str:
    """
    Load a text file and replace email placeholders.
    
    Args:
        filepath: Path to file
        
    Returns:
        File content with placeholders replaced
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    return replace_email_placeholders(content)


# ============================================================================
# Utility functions for one-time replacement of hardcoded emails (script use)
# ============================================================================

OLD_EMAILS = [
    "qwuqwuqwu@gmail.com",
    "cc9008@nyu.edu",
]

PLACEHOLDER_MAP = {
    "qwuqwuqwu@gmail.com": EMAIL_PLACEHOLDER,
    "cc9008@nyu.edu": EMAIL_CC_PLACEHOLDER,
}


def convert_file_to_placeholders(filepath: str, dry_run: bool = False) -> bool:
    """
    Convert hardcoded emails in a file to placeholders.
    
    Args:
        filepath: Path to file
        dry_run: If True, only check without modifying
        
    Returns:
        Whether the file was modified
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  Unable to read file {filepath}: {e}")
        return False
    
    original_content = content
    
    for old_email, placeholder in PLACEHOLDER_MAP.items():
        content = content.replace(old_email, placeholder)
    
    if content != original_content:
        if not dry_run:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
        return True
    
    return False


def convert_directory_to_placeholders(
    directory: str, 
    extensions: List[str] = None,
    dry_run: bool = False
) -> List[str]:
    """
    Recursively convert hardcoded emails to placeholders in all files in a directory.
    
    Args:
        directory: Directory path
        extensions: List of file extensions to process, None means all
        dry_run: If True, only check without modifying
        
    Returns:
        List of modified files
    """
    if extensions is None:
        extensions = ['.json', '.py', '.md', '.txt', '.meta', '.yaml', '.yml']
    
    modified_files = []
    
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if any(filename.endswith(ext) for ext in extensions):
                filepath = os.path.join(root, filename)
                if convert_file_to_placeholders(filepath, dry_run):
                    modified_files.append(filepath)
                    action = "Will modify" if dry_run else "Modified"
                    print(f"  {action}: {filepath}")
    
    return modified_files


# ============================================================================
# Command line tool
# ============================================================================

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description="RA-ProAgent Email Placeholder Tool"
    )
    parser.add_argument(
        "action",
        choices=["convert", "check", "test"],
        help="convert: Convert hardcoded emails to placeholders; check: Check without modifying; test: Test environment variables"
    )
    parser.add_argument(
        "--dir",
        default="./apa_case_storage",
        help="Target directory (default: ./apa_case_storage)"
    )
    
    args = parser.parse_args()
    
    if args.action == "test":
        print("Testing environment variable configuration...")
        try:
            primary, cc = get_user_emails()
            print(f"✓ USER_EMAIL: {primary}")
            print(f"✓ USER_EMAIL_CC: {cc}")
            print("\nEnvironment variables configured correctly!")
        except ValueError as e:
            print(f"✗ Error: {e}")
            
    elif args.action in ["convert", "check"]:
        dry_run = (args.action == "check")
        mode = "Checking" if dry_run else "Converting"
        
        print(f"{mode} directory: {args.dir}")
        print(f"Replacing {OLD_EMAILS} with placeholders\n")
        
        if not os.path.isdir(args.dir):
            print(f"Error: Directory does not exist: {args.dir}")
            exit(1)
            
        modified = convert_directory_to_placeholders(args.dir, dry_run=dry_run)
        
        print(f"\n{'Will modify' if dry_run else 'Modified'} {len(modified)} files")
        
        if dry_run and modified:
            print("\nRun 'python email_utils.py convert' to apply changes")
