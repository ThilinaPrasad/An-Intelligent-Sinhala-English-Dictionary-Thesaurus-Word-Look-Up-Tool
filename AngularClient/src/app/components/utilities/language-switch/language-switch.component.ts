import {Component, Input, OnInit} from '@angular/core';
import {TranslateService} from '@ngx-translate/core';

@Component({
  selector: 'app-language-switch',
  templateUrl: './language-switch.component.html',
  styleUrls: ['./language-switch.component.css']
})
export class LanguageSwitchComponent implements OnInit {

  @Input()
  private textColor;

  @Input()
  private activeBorderColor;

  public language = 'en';

  constructor(private translateService: TranslateService) {
    const savedLang = localStorage.getItem('lang');
    if (savedLang) {
      this.language = savedLang;
    }
  }

  ngOnInit() {
  }

  changeLang(lang) {
    this.language = lang;
    this.translateService.use(lang);
    this.translateService.setDefaultLang(lang);
    localStorage.setItem('lang', lang);
  }

}
