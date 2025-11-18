describe('My First Test', () => {
  it('Visits the app', () => {
    cy.visit('http://localhost:3000');
    cy.contains('Welcome');
  });

  it('Clicks a button', () => {
    cy.visit('http://localhost:3000');
    cy.get('button').first().click();
  });
});
