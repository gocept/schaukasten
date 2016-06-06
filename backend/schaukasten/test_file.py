from schaukasten.file import File, Content
import transaction


def test_file__File__1(database):
    """It creates a File in the database and connects it with a Content."""
    content = Content.create(raw_content=b"Content of test file.")
    file_ = File.create(
        filename="content_test.txt",
        mimetype="test/plain",
        content=content,
    )

    transaction.commit()
    assert 1 == content.identifier
    assert 1 == file_.content_id


def test_file__Content__1():
    """It returns a md5 hash of the raw_content."""
    content = Content.create(raw_content="Content of test file.")
    assert '37856c1f-9ae4-2663-dec7-f20430d46cf6' == str(content.hash)
