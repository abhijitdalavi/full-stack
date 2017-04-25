import { MappyPage } from './app.po';

describe('mappy App', () => {
  let page: MappyPage;

  beforeEach(() => {
    page = new MappyPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
