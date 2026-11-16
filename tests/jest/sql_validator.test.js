const { inspectDdlSafety } = require('../../js/sql_validator');

describe('SQL DDL Validator', () => {
  it('flags destructive drop statements', () => {
    const res = inspectDdlSafety('DROP TABLE users;');
    expect(res.isSafe).toBe(false);
    expect(res.warnings).toContain('DROP TABLE');
  });
  it('approves safe create table DDL', () => {
    const res = inspectDdlSafety('CREATE TABLE posts (id INT);');
    expect(res.isSafe).toBe(true);
  });
});
