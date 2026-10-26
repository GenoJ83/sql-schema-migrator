function inspectDdlSafety(sql) {
  if (!sql) return { isSafe: true, warnings: [] };
  const upper = sql.toUpperCase();
  const dangerous = ['DROP TABLE', 'TRUNCATE', 'ALTER TABLE DROP COLUMN'];
  const warnings = dangerous.filter((d) => upper.includes(d));
  return { isSafe: warnings.length === 0, warnings };
}
module.exports = { inspectDdlSafety };
